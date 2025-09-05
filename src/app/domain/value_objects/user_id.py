from dataclasses import dataclass

from app.domain.common.value_objects import ValueObject


@dataclass(slots=True, frozen=True)
class UserId(ValueObject[int]):
    value: int
