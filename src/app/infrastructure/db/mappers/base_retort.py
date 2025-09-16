from adaptix import P, Retort, loader

from app.domain.entities.user import User
from app.domain.value_objects.user_id import UserId
from app.domain.value_objects.user_password_hash import UserPasswordHash
from app.domain.value_objects.username import Username

base_retort = Retort(
    recipe=[
        loader(P[User].id, lambda x: UserId(x)),
        loader(P[User].username, lambda x: Username(x)),
        loader(P[User].password_hash, lambda x: UserPasswordHash(x)),

    ],
)
