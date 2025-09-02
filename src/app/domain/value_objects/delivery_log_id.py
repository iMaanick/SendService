from dataclasses import dataclass

from app.domain.common.value_objects import ValueObject


@dataclass(frozen=True)
class DeliveryLogId(ValueObject[int]):
    value: int
