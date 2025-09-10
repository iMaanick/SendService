from adaptix._internal.conversion.facade.provider import coercer
from adaptix._internal.conversion.facade.retort import ConversionRetort

from app.domain.value_objects.user_id import UserId
from app.domain.value_objects.user_password_hash import UserPasswordHash
from app.domain.value_objects.username import Username

from_orm_retort = ConversionRetort(
    recipe=[
        coercer(int, UserId, lambda x: UserId(x)),
        coercer(str, Username, lambda x: Username(x)),
        coercer(bytes, UserPasswordHash, lambda x: UserPasswordHash(x)),
    ],
)
