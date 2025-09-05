from dataclasses import dataclass

from app.domain.common.value_objects import ValueObject


@dataclass(frozen=True, slots=True)
class ContactId(ValueObject[int]):
    value: int
