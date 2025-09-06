from dataclasses import dataclass

from app.domain.common.entity import BaseEntityObject
from app.domain.shared.user_role import UserRole
from app.domain.value_objects.user_id import UserId
from app.domain.value_objects.user_password_hash import UserPasswordHash
from app.domain.value_objects.username import Username


@dataclass(slots=True, frozen=True)
class User(BaseEntityObject):
    id: UserId
    username: Username
    password_hash: UserPasswordHash
    role: UserRole
    is_active: bool
