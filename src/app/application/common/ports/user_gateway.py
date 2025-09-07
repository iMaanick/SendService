from abc import abstractmethod
from typing import Protocol

from app.domain.entities.user import User
from app.domain.value_objects.user_id import UserId
from app.domain.value_objects.username import Username


class UserGateway(Protocol):
    @abstractmethod
    def add(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def read_by_id(self, user_id: UserId) -> User | None:
        raise NotImplementedError

    @abstractmethod
    async def read_by_username(
            self,
            username: Username,
    ) -> User | None:
        raise NotImplementedError
