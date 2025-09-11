from sqlalchemy.exc import SQLAlchemyError

from app.application.common.exceptions.ports import CommitError
from app.application.common.ports.transactionmanager import TransactionManager
from app.infrastructure.db.types import MainAsyncSession


class SqlaTransactionManager(TransactionManager):
    def __init__(self, session: MainAsyncSession):
        self.session = session

    async def commit(self) -> None:
        try:
            await self.session.commit()
        except SQLAlchemyError as err:
            raise CommitError from err
