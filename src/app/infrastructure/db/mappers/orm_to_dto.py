from adaptix._internal.conversion.facade.provider import coercer, allow_unlinked_optional
from adaptix._internal.conversion.facade.retort import ConversionRetort

from app.domain.value_objects.user_password_hash import UserPasswordHash
from app.domain.value_objects.username import Username

dto_to_orm_retort = ConversionRetort(
    recipe=[
        allow_unlinked_optional("id"),
        coercer(Username, str, lambda x: x.value),
        coercer(UserPasswordHash, bytes, lambda x: x.value),
        coercer(int | None, int, lambda x: None)
    ]
)
