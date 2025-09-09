from dishka import Provider, Scope, from_context, provide

from app.bootstrap.configs import DatabaseConfig, PasswordConfig
from app.infrastructure.adapters.password_hasher_bcrypt import PasswordPepper


class AppConfigProvider(Provider):
    scope = Scope.APP

    database_config = from_context(DatabaseConfig)
    password = from_context(PasswordConfig)

    @provide
    def provide_password_pepper(self, config: PasswordConfig) -> PasswordPepper:
        return PasswordPepper(config.pepper)