from dishka import Provider, Scope, from_context

from app.bootstrap.configs import DatabaseConfig


class AppConfigProvider(Provider):
    scope = Scope.APP

    database_config = from_context(DatabaseConfig)
