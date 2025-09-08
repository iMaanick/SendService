from dataclasses import dataclass

from app.application.common.ports.user_dto import CreateUser
from app.application.common.ports.user_gateway import UserGateway
from app.domain.entities.user import User
from app.domain.value_objects.user_id import UserId
from app.domain.value_objects.username import Username
from app.infrastructure.db.types import MainAsyncSession


@dataclass(slots=True, frozen=True)
class UserSQLGateway(UserGateway):
    session: MainAsyncSession

    def add(self, user: CreateUser) -> User:
        raise NotImplementedError

    async def read_by_id(self, user_id: UserId) -> User | None:
        raise NotImplementedError

    async def read_by_username(
            self,
            username: Username,
    ) -> User | None:
        raise NotImplementedError
