import logging
from collections.abc import AsyncIterable, AsyncIterator
from typing import cast

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.bootstrap.configs import DatabaseConfig
from app.infrastructure.db.types import MainAsyncSession

logger = logging.getLogger(__name__)


class PersistenceProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.APP)
    async def engine(
            self, config: DatabaseConfig,
    ) -> AsyncIterator[AsyncEngine]:
        engine = create_async_engine(config.uri)
        yield engine
        await engine.dispose()

    @provide(scope=Scope.APP)
    def get_sessionmaker(
            self, engine: AsyncEngine,
    ) -> async_sessionmaker[AsyncSession]:
        factory = async_sessionmaker(
            engine,
            expire_on_commit=False,
            class_=AsyncSession,
            autoflush=False,
        )
        logger.debug("Session provider was initialized")
        return factory

    @provide
    async def get_session(
            self, factory: async_sessionmaker[AsyncSession],
    ) -> AsyncIterable[MainAsyncSession]:
        async with factory() as session:
            yield cast(MainAsyncSession, session)
