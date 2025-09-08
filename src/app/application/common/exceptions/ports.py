from dataclasses import dataclass

from app.application.common.exceptions.base import ApplicationError


@dataclass(slots=True, frozen=True)
class UnexpectedError(ApplicationError):
    pass


@dataclass(slots=True, frozen=True)
class CommitError(UnexpectedError):
    pass


@dataclass(slots=True, frozen=True)
class FlushError(UnexpectedError):
    pass


@dataclass(slots=True, frozen=True)
class RepoError(UnexpectedError):
    pass
