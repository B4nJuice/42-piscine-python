from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0, le=10)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    def __str__(self) -> str:
        infos: list[str] = [
                f"ID: {self.contact_id}",
                f"Type: {self.contact_type.value}",
                f"Location: {self.location}",
                f"Date: {self.timestamp}",
                f"Signal: {self.signal_strength:.1f}/10",
                f"Duration: {self.duration_minutes}\
 minutes{'s'*(self.duration_minutes > 1)}",
                f"Witnesses: {self.witness_count}",
                f"Status: {'Verified' if self.is_verified else 'Unverified'}"
        ]

        if self.message_received:
            infos.append(f"Message: \'{self.message_received}\'")

        return "\n".join(infos)

    @model_validator(mode='after')
    def validate_contact(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with \"AC\".")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified.")
        if self.contact_type == ContactType.TELEPATHIC and\
                self.witness_count < 3:
            raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                    "Strong signals (> 7.0) should include received messages"
                )

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    print()

    try:
        print("Valid contact report:")

        valid_contact: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )

        print(valid_contact)
    except (ValidationError, ValueError) as e:
        for error in e.errors():
            print(f"- {error.get('msg')}")

    print()

    print("======================================")

    print()

    try:
        print("Trying creating invalid contact...")

        invalid_contact: AlienContact = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2
        )

        print(invalid_contact)
    except (ValidationError, ValueError) as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"- {error.get('msg')}")


if __name__ == "__main__":
    main()
