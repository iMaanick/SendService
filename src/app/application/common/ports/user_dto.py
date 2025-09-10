from dataclasses import dataclass

from app.domain.shared.user_role import UserRole
from app.domain.value_objects.user_password_hash import UserPasswordHash
from app.domain.value_objects.username import Username


@dataclass(slots=True)
class CreateUser:
    username: Username
    password_hash: UserPasswordHash
    role: UserRole
    is_active: bool
