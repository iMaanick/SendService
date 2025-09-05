from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class BaseEntityObject:

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        ...
