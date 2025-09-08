import logging
from dataclasses import dataclass

from app.application.common.ports.uow import UoW
from app.application.common.ports.user_gateway import UserGateway
from app.domain.value_objects.raw_password import RawPassword
from app.domain.value_objects.username import Username

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class SignUpRequest:
    username: str
    password: str

@dataclass(slots=True, frozen=True)
class SignUpResponse:
    id: int

@dataclass(slots=True, frozen=True)
class SignUpUseCase:
    user_factory: UserFactory
    user_gateway: UserGateway
    uow: UoW


    async def __call__(self, request_data: SignUpRequest) -> SignUpResponse:

        logger.info("Sign up: started. Username: '%s'.", request_data.username)

        username = Username(request_data.username)
        password = RawPassword(request_data.password)

        user = self.user_factory.create_user(username, password)

        self.user_gateway.add(user)

        await self.uow.commit()

        logger.info("Sign up: done. Username: '%s'.", user.username.value)
        return SignUpResponse(id=user.id_.value)
