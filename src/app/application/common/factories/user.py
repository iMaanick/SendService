from app.application.common.ports.user_dto import CreateUser
from app.domain.exceptions.user import RoleAssignmentNotPermittedError
from app.domain.ports.password_hasher import PasswordHasher
from app.domain.shared.user_role import UserRole
from app.domain.value_objects.raw_password import RawPassword
from app.domain.value_objects.user_password_hash import UserPasswordHash
from app.domain.value_objects.username import Username


class UserFactory:
    def __init__(
            self,
            password_hasher: PasswordHasher,
    ) -> None:
        self._password_hasher = password_hasher

    def create_user(
            self,
            username: Username,
            raw_password: RawPassword,
            role: UserRole = UserRole.USER,
            *,
            is_active: bool = True,
    ) -> CreateUser:
        if not role.is_assignable:
            raise RoleAssignmentNotPermittedError(role)

        password_hash = UserPasswordHash(
            self._password_hasher.hash(raw_password),
        )
        return CreateUser(
            username=username,
            password_hash=password_hash,
            role=role,
            is_active=is_active,
        )
