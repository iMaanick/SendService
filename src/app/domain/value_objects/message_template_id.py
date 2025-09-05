from dataclasses import dataclass

from app.domain.common.value_objects import ValueObject


@dataclass(slots=True, frozen=True)
class MessageTemplateId(ValueObject[int]):
    value: int
