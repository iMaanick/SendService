from sqlalchemy import BigInteger, Boolean, Enum, LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.shared.user_role import UserRole
from app.domain.value_objects.username import Username
from app.infrastructure.db.models import BaseModel


class UserORM(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    username: Mapped[str] = mapped_column(
        String(Username.max_len),
        nullable=False,
        unique=True,
    )
    password_hash: Mapped[bytes] = mapped_column(
        LargeBinary,
        nullable=False,
    )
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="userrole"),
        default=UserRole.USER,
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
