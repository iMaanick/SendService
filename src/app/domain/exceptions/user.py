from dataclasses import dataclass

from app.domain.common.exceptions import DomainError
from app.domain.shared.user_role import UserRole


@dataclass(slots=True, frozen=True)
class RoleAssignmentNotPermittedError(DomainError):
    role: UserRole

    @property
    def title(self) -> str:
        return f"Assignment of role {self.role} is not permitted."


@dataclass(slots=True, frozen=True)
class UsernameAlreadyExistsError(DomainError):
    username: str

    @property
    def title(self) -> str:
        return f"User with username {self.username} already exists."
