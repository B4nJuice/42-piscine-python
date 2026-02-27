from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True

    def __str__(self) -> str:
        return f"{self.name} ({self.rank.value}) - {self.specialization}"


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_day: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1, le=10000)

    def __str__(self) -> str:
        infos: list[str] = [
                f"Mission: {self.mission_name}",
                f"ID: {self.mission_id}",
                f"Destination: {self.destination}",
                f"Duration: {self.duration_day}{'s'*(self.duration_day > 1)}",
                f"Budget: ${self.budget_millions:.1f}M",
                f"Crew size: {len(self.crew)}",
                "Crew members:"
        ]

        crew_infos: list[str] = [
                "- " + member.__str__() for member in self.crew
            ]

        infos += crew_infos

        return "\n".join(infos)

    @model_validator(mode="after")
    def mission_validator(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")

        have_commander_or_captain: bool = False

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
            match member.rank:
                case Rank.CAPTAIN | Rank.COMMANDER:
                    have_commander_or_captain = True

        if not have_commander_or_captain:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_day > 365:
            experienced_member: int = len(
                    [member for member in self.crew
                        if member.years_experience >= 5]
                )
            if experienced_member / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions\
 (> 365 days) need 50% experienced crew (5+ years)")

        return self


def main() -> None:
    sarah: CrewMember = CrewMember(
            member_id="sarah",
            name="Sarah Connor",
            age=45,
            rank=Rank.COMMANDER,
            specialization="Mission Command",
            years_experience=10
        )

    john: CrewMember = CrewMember(
            member_id="john",
            name="John Smith",
            age=45,
            rank=Rank.LIEUTENANT,
            specialization="Navigation",
            years_experience=5
        )

    alice: CrewMember = CrewMember(
            member_id="alice",
            name="Alice Johnson",
            age=45,
            rank=Rank.OFFICER,
            specialization="Engineering",
            years_experience=6
        )

    mars_crew: list[CrewMember] = [sarah, john, alice]

    mars_mission: SpaceMission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_day=900,
        crew=mars_crew,
        budget_millions=2500
    )

    print(mars_mission)


if __name__ == "__main__":
    main()
