import re
from dataclasses import dataclass
from typing import ClassVar

from app.domain.common.exceptions import DomainError
from app.domain.common.value_objects import BaseValueObject


@dataclass(slots=True, frozen=True)
class InvalidEmailLengthError(DomainError):
    min_len: int
    max_len: int

    @property
    def title(self) -> str:
        return (
            f"Username must be between "
            f"{self.min_len} and "
            f"{self.max_len} characters."
        )


@dataclass(slots=True, frozen=True)
class InvalidUsernamePatternError(DomainError):

    @property
    def title(self) -> str:
        return "Username must end with a letter (A-Z, a-z) or a digit (0-9)."


@dataclass(slots=True, frozen=True, repr=False)
class Username(BaseValueObject):
    min_len: ClassVar[int] = 5
    max_len: ClassVar[int] = 20

    pattern: ClassVar[re.Pattern[str]] = re.compile(
        r"^[a-zA-Z0-9]",
    )

    value: str

    def _validate(self) -> None:
        self._validate_username_length(self.value)
        self._validate_username_pattern(self.value)

    def _validate_username_length(self, username_value: str) -> None:
        if (
                len(username_value) < self.min_len
                or
                len(username_value) > self.max_len
        ):
            raise InvalidEmailLengthError(self.min_len, self.max_len)

    def _validate_username_pattern(self, username_value: str) -> None:
        if not re.match(self.pattern, username_value):
            raise InvalidUsernamePatternError
