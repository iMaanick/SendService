from dataclasses import dataclass

from app.application.common.ports.user_dto import CreateUser
from app.application.common.ports.user_gateway import UserGateway
from app.domain.entities.user import User
from app.domain.value_objects.user_id import UserId
from app.domain.value_objects.username import Username
from app.infrastructure.db.mappers.dto_to_orm import dto_to_orm_retort
from app.infrastructure.db.mappers.from_orm import from_orm_retort
from app.infrastructure.db.models import UserORM
from app.infrastructure.db.types import MainAsyncSession


@dataclass(slots=True, frozen=True)
class UserSQLGateway(UserGateway):
    session: MainAsyncSession

    async def add(self, user: CreateUser) -> User:
        converter = dto_to_orm_retort.get_converter(CreateUser, UserORM)
        new_user = converter(user)
        self.session.add(new_user)
        await self.session.flush()
        user_converter = from_orm_retort.get_converter(UserORM, User)
        return user_converter(new_user)

    async def read_by_id(self, user_id: UserId) -> User | None:
        raise NotImplementedError

    async def read_by_username(
            self,
            username: Username,
    ) -> User | None:
        raise NotImplementedError
