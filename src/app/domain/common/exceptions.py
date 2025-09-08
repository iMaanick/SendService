from dataclasses import dataclass
from typing import ClassVar

from app.domain.shared.user_role import UserRole


@dataclass(slots=True, frozen=True)
class AppError(Exception):
    status: ClassVar[int] = 500

    @property
    def title(self) -> str:
        return "An app error occurred"


@dataclass(slots=True, frozen=True)
class DomainError(AppError):

    @property
    def title(self) -> str:
        return "A domain error occurred"


@dataclass(slots=True, frozen=True)
class RoleAssignmentNotPermittedError(AppError):
    role: UserRole

    @property
    def title(self) -> str:
        return f"Assignment of role {self.role} is not permitted."
