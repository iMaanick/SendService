from dataclasses import dataclass

from adaptix import Retort
from sqlalchemy.dialects.postgresql import insert

from app.application.common.ports.user_dto import CreateUser
from app.application.common.ports.user_gateway import UserGateway
from app.domain.entities.user import User
from app.domain.value_objects.user_id import UserId
from app.domain.value_objects.username import Username
from app.infrastructure.db.models import users_table
from app.infrastructure.db.types import MainAsyncSession


@dataclass(slots=True, frozen=True)
class UserSQLGateway(UserGateway):
    session: MainAsyncSession
    retort: Retort

    async def add(self, user: CreateUser) -> User:
        stmt = (
            insert(users_table)
            .values(
                username=user.username.value,
                password_hash=user.password_hash.value,
                role=user.role,
                is_active=user.is_active,
            )
            .returning(users_table)
        )

        result = await self.session.execute(stmt)
        row = result.mappings().one()
        return self.retort.load(row, User)

    async def read_by_id(self, user_id: UserId) -> User | None:
        raise NotImplementedError

    async def read_by_username(
            self,
            username: Username,
    ) -> User | None:
        raise NotImplementedError
