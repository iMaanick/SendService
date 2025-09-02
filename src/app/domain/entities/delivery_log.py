from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum

from app.domain.common.exceptions import DomainError
from app.domain.shared.channel import ChannelType


class DeliveryStatus(str, Enum):
    PENDING = "pending"
    SENT = "sent"
    DELIVERED = "delivered"
    FAILED = "failed"


@dataclass(frozen=True, slots=True)
class DeliveryLog:
    id: int
    campaign_id: int
    subscriber_id: int
    channel: ChannelType
    status: DeliveryStatus
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))


@dataclass(slots=True)
class DeliveryLogError(DomainError):
    pass
