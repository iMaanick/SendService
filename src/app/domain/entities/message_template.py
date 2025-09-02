from dataclasses import dataclass, field

from app.domain.value_objects.message_template_id import MessageTemplateId


@dataclass(frozen=True, slots=True)
class MessageTemplate:
    id: MessageTemplateId
    title: str
    body: str
    variables: list[str] = field(default_factory=list)
