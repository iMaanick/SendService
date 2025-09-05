from abc import ABC
from dataclasses import dataclass
from typing import Any, TypeVar

V = TypeVar("V", bound=Any)


@dataclass(slots=True, frozen=True)
class BaseValueObject:

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        ...


@dataclass(slots=True, frozen=True)
class ValueObject[V](BaseValueObject, ABC):
    value: V

    def to_raw(self) -> V:
        return self.value
