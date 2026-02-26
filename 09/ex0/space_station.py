from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0, le=1)
    oxygen_level: float = Field(..., ge=0, le=1)
    last_maintenance: datetime
    is_operational: Optional[bool] = True
    notes: Optional[str] = Field(None, max_length=200)

    def __str__(self) -> str:

        status = 'Operational' if self.is_operational else 'Down'

        infos: str = [f"ID: {self.station_id}",
                      f"Name: {self.name}",
                      f"Crew: {self.crew_size} people",
                      f"Power: {self.power_level*100:.1f}%",
                      f"Oxygen: {self.oxygen_level*100:.1f}%",
                      f"Status: {status}"]

        if self.notes:
            infos.append(f"Notes: {self.notes}")

        return "\n".join(infos)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    print()

    try:
        valid_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=0.855,
            oxygen_level=0.923,
            last_maintenance=datetime.now()
        )

        print("Valid station created:")
        print(valid_station)
    except ValidationError as e:
        print(e)

    print()

    print("========================================")

    print()

    try:
        print("Trying creating invalid space station...")
        invalid_station: SpaceStation = SpaceStation(
            station_id="ISS002",
            name="Fake International Space Station",
            crew_size=50,
            power_level=1,
            oxygen_level=1,
            last_maintenance=datetime.now()
        )

        print(invalid_station)
    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()
