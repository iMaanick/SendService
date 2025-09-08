from dataclasses import dataclass

from app.domain.common.exceptions import AppError


@dataclass(slots=True, frozen=True)
class ApplicationError(AppError):

    @property
    def title(self) -> str:
        return "An application error occurred"
