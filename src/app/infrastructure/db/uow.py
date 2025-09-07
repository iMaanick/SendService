from dataclasses import dataclass

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.common.exceptions import CommitError, FlushError
from app.application.common.ports.uow import UoW


@dataclass(slots=True, frozen=True)
class SQLAlchemyUoW(UoW):
    session: AsyncSession

    async def commit(self) -> None:
        try:
            await self.session.commit()
        except SQLAlchemyError as err:
            raise CommitError from err

    async def flush(self) -> None:
        try:
            await self.session.flush()
        except SQLAlchemyError as err:
            raise FlushError from err
