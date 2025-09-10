from dishka import Provider, Scope, WithParents, provide, provide_all

from app.application.common.factories.user import UserFactory
from app.application.use_cases.sign_up import SignUpUseCase
from app.bootstrap.ioc.converters import (
    Dst_co,
    FromOrmConverter,
    Src_contra,
    ToOrmConverter,
)
from app.infrastructure.db.mappers.from_orm import from_orm_retort
from app.infrastructure.db.mappers.to_orm import dto_to_orm_retort
from app.infrastructure.db.uow import SQLAlchemyUoW
from app.infrastructure.db.user_gateway import UserSQLGateway


class ApplicationProvider(Provider):
    gateways = provide_all(
        WithParents[UserSQLGateway],
        WithParents[SQLAlchemyUoW],
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

    @provide(scope=Scope.APP)
    def to_orm_converter(
            self,
            src_type: type[Src_contra],
            dst_type: type[Dst_co],
    ) -> ToOrmConverter[Src_contra, Dst_co]:
        return dto_to_orm_retort.get_converter(src_type, dst_type)

    @provide(scope=Scope.APP)
    def from_orm_converter(
            self,
            src_type: type[Src_contra],
            dst_type: type[Dst_co],
    ) -> FromOrmConverter[Src_contra, Dst_co]:
        return from_orm_retort.get_converter(src_type, dst_type)
