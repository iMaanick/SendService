from dataclasses import dataclass

from app.domain.common.exceptions import DomainError
from app.domain.common.value_objects import BaseValueObject
from app.domain.shared.channel import ChannelType


@dataclass(slots=True)
class InvalidContactError(DomainError):
    contact: str
    text: str

    @property
    def title(self) -> str:
        return self.text


@dataclass(frozen=True, slots=True)
class Contact(BaseValueObject):
    id: int
    contact: str
    channel: ChannelType

    def _validate(self) -> None:

        if not self.contact or not self.contact.strip():
            raise InvalidContactError(
                self.contact,
                f"Contact cannot be empty for channel {self.channel}",
            )

        if self.channel not in {"email", "telegram", "vk"}:
            raise InvalidContactError(
                self.contact,
                f"Unknown channel {self.channel}",
            )

    def __str__(self) -> str:
        return f"{self.contact} ({self.channel})"
