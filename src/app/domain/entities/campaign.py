from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

from app.domain.common.exceptions import DomainError
from app.domain.entities.subscriber import Subscriber
from app.domain.shared.channel import ChannelType


class CampaignStatus(str, Enum):
    DRAFT = "draft"
    SCHEDULED = "scheduled"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(frozen=True, slots=True)
class Campaign:
    id: int
    name: str
    message_template_id: str
    schedule: datetime
    status: CampaignStatus
    channels: list[ChannelType] = field(default_factory=list)
    subscribers: list[Subscriber] = field(default_factory=list)


@dataclass(slots=True)
class CampaignValidationError(DomainError):
    text: str

    @property
    def title(self) -> str:
        return self.text
