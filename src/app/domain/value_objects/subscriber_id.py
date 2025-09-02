from dataclasses import dataclass

from app.domain.common.value_objects import ValueObject


@dataclass(frozen=True)
class SubscriberId(ValueObject[int]):
    value: int
