from dataclasses import dataclass, field
from enum import Enum

from app.domain.common.exceptions import DomainError
from app.domain.entities.contact import Contact
from app.domain.value_objects.subscriber_id import SubscriberId


class SubscriberStatus(str, Enum):
    ACTIVE = "active"
    UNSUBSCRIBED = "unsubscribed"
    BOUNCED = "bounced"


@dataclass(frozen=True, slots=True)
class Subscriber:
    id: SubscriberId
    status: SubscriberStatus
    contacts: list[Contact] = field(default_factory=list)
    preferred_channels: list[str] = field(default_factory=list)


@dataclass(slots=True)
class SubscriberValidationError(DomainError):
    pass
