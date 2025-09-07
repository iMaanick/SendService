import logging

from dishka import AsyncContainer, make_async_container

from app.bootstrap.configs import DatabaseConfig
from app.bootstrap.ioc.application import ApplicationProvider
from app.bootstrap.ioc.config import AppConfigProvider
from app.bootstrap.ioc.infrastructure import PersistenceProvider

logger = logging.getLogger(__name__)


def fastapi_container(
        database_config: DatabaseConfig,
) -> AsyncContainer:
    logger.info("Fastapi DI setup")

    return make_async_container(
        AppConfigProvider(),
        PersistenceProvider(),
        ApplicationProvider(),
        context={
            DatabaseConfig: database_config,

        },
    )
