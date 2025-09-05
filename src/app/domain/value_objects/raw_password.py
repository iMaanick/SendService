from dataclasses import dataclass
from typing import ClassVar

from app.domain.common.exceptions import DomainError
from app.domain.common.value_objects import BaseValueObject


@dataclass(slots=True, frozen=True)
class InvalidPasswordError(DomainError):
    min_len: int

    @property
    def title(self) -> str:
        return f"Password must be at least {self.min_len} characters long."


@dataclass(slots=True, frozen=True, repr=False)
class RawPassword(BaseValueObject):
    MIN_LEN: ClassVar[int] = 6

    value: str

    def _validate(self) -> None:
        self._validate_password_length(self.value)

    def _validate_password_length(self, password_value: str) -> None:
        if len(password_value) < self.MIN_LEN:
            raise InvalidPasswordError(self.MIN_LEN)
