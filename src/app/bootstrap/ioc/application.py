from dishka import Provider, Scope, WithParents, provide, provide_all

from app.application.common.factories.user import UserFactory
from app.application.use_cases.sign_up import SignUpUseCase
from app.infrastructure.db.flusher_sqla import SqlaMainFlusher
from app.infrastructure.db.mappers.from_orm import from_orm_retort
from app.infrastructure.db.mappers.to_orm import dto_to_orm_retort
from app.infrastructure.db.transaction_manager_sqla import (
    SqlaTransactionManager,
)
from app.infrastructure.db.user_gateway import UserSQLGateway


class ApplicationProvider(Provider):
    gateways = provide_all(
        WithParents[UserSQLGateway],
        WithParents[SqlaTransactionManager],
        WithParents[SqlaMainFlusher],
        scope=Scope.REQUEST,
    )

    use_cases = provide_all(
        SignUpUseCase,
        scope=Scope.REQUEST,
    )

    factories_services = provide_all(
        UserFactory,
        scope=Scope.REQUEST,
    )