import logging

from adaptix import Retort
from dishka import AsyncContainer, make_async_container

from app.bootstrap.configs import Config, DatabaseConfig, PasswordConfig
from app.bootstrap.ioc.application import ApplicationProvider
from app.bootstrap.ioc.config import AppConfigProvider
from app.bootstrap.ioc.domain import DomainProvider
from app.bootstrap.ioc.infrastructure import InfrastructureProvider

logger = logging.getLogger(__name__)


def fastapi_container(
        config: Config,
        base_retort: Retort,
) -> AsyncContainer:
    logger.info("Fastapi DI setup")

    return make_async_container(
        AppConfigProvider(),
        InfrastructureProvider(),
        ApplicationProvider(),
        DomainProvider(),
        context={
            DatabaseConfig: config.database,
            PasswordConfig: config.password,
            Retort: base_retort,
        },
    )
