from dishka import Provider, Scope, provide

from app.domain.ports.password_hasher import PasswordHasher
from app.infrastructure.adapters.password_hasher_bcrypt import (
    BcryptPasswordHasher,
)


class DomainProvider(Provider):
    scope = Scope.REQUEST

    # Ports
    password_hasher = provide(
        source=BcryptPasswordHasher,
        provides=PasswordHasher,
    )
