from dishka import Provider, Scope, WithParents, provide_all

from app.infrastructure.db.uow import SQLAlchemyUoW
from app.infrastructure.db.user_gateway import UserSQLGateway


class ApplicationProvider(Provider):
    gateways = provide_all(
        WithParents[UserSQLGateway],
        WithParents[SQLAlchemyUoW],
        scope=Scope.REQUEST,
    )
