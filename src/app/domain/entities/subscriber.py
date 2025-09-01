from dataclasses import dataclass, field
from enum import Enum

from app.domain.common.exceptions import DomainError
from app.domain.value_objects.contact import Contact


class SubscriberStatus(str, Enum):
    ACTIVE = "active"
    UNSUBSCRIBED = "unsubscribed"
    BOUNCED = "bounced"


@dataclass(frozen=True, slots=True)
class Subscriber:
    id: str
    contacts: list[Contact] = field(default_factory=list)
    preferred_channels: list[str] = field(default_factory=list)
    status: str = field(default=SubscriberStatus.ACTIVE)


@dataclass(slots=True)
class SubscriberValidationError(DomainError):
    pass
