from dataclasses import dataclass
from datetime import UTC, datetime

from app.domain.entities.campaign import (
    Campaign,
    CampaignStatus,
    CampaignValidationError,
)
from app.domain.entities.subscriber import Subscriber


@dataclass(slots=True, frozen=True)
class CampaignMissingChannelsError(CampaignValidationError):
    text: str = "Campaign must have at least one channel"


@dataclass(slots=True, frozen=True)
class CampaignInvalidScheduleError(CampaignValidationError):
    text: str = "Campaign schedule must be in the future"

class CampaignService:

    @staticmethod
    def schedule_campaign(campaign: Campaign) -> Campaign:
        if not campaign.channels:
            raise CampaignMissingChannelsError

        if campaign.schedule < datetime.now(UTC):
            raise CampaignInvalidScheduleError

        return Campaign(
            id=campaign.id,
            name=campaign.name,
            message_template_id=campaign.message_template_id,
            channels=campaign.channels,
            schedule=campaign.schedule,
            status=CampaignStatus.SCHEDULED,
            subscribers=campaign.subscribers,
        )
    @staticmethod
    def add_subscriber(campaign: Campaign, subscriber: Subscriber) -> Campaign:
        updated_subscribers = [*campaign.subscribers, subscriber]
        return Campaign(
            id=campaign.id,
            name=campaign.name,
            message_template_id=campaign.message_template_id,
            channels=campaign.channels,
            schedule=campaign.schedule,
            status=campaign.status,
            subscribers=updated_subscribers,
        )
