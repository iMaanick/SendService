import logging
from collections.abc import Mapping
from typing import Any, cast

from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.application.common.exceptions.ports import FlushError
from app.application.common.ports.flusher import Flusher
from app.domain.exceptions.user import UsernameAlreadyExistsError
from app.infrastructure.db.types import MainAsyncSession

logger = logging.getLogger(__name__)


class SqlaMainFlusher(Flusher):
    def __init__(self, session: MainAsyncSession):
        self.session = session

    async def flush(self) -> None:
        try:
            await self.session.flush()
        except IntegrityError as error:
            if "uq_users_username" in str(error):
                params: Mapping[str, Any] = cast(
                    Mapping[str, Any],
                    error.params,
                )
                username = str(params.get("username", "unknown"))
                raise UsernameAlreadyExistsError(username) from error
        except SQLAlchemyError as err:
            raise FlushError from err
