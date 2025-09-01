from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, TypeVar

V = TypeVar("V", bound=Any)


@dataclass(frozen=True)
class BaseValueObject(ABC):

    def __post_init__(self) -> None:
        self._validate()

    @abstractmethod
    def _validate(self) -> None:
        raise NotImplementedError


@dataclass(frozen=True)
class ValueObject[V](BaseValueObject, ABC):
    value: V

    def to_raw(self) -> V:
        return self.value
