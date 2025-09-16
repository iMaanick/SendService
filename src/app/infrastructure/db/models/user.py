from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Enum,
    LargeBinary,
    String,
    Table,
)

from app.domain.shared.user_role import UserRole
from app.domain.value_objects.username import Username
from app.infrastructure.db.models.base import metadata

users_table = Table(
    "users",
    metadata,
    Column(
        "id",
        BigInteger,
        primary_key=True,
        autoincrement=True,
    ),
    Column(
        "username",
        String(Username.max_len),
        nullable=False,
        unique=True,
    ),
    Column(
        "password_hash",
        LargeBinary,
        nullable=False,
    ),
    Column(
        "role",
        Enum(UserRole, name="userrole"),
        nullable=False,
        default=UserRole.USER,
    ),
    Column(
        "is_active",
        Boolean,
        nullable=False,
        default=True,
    ),
)
