from app.domain.common.exceptions import AppError


class ApplicationError(AppError):

    @property
    def title(self) -> str:
        return "An application error occurred"


class UnexpectedError(ApplicationError):
    pass


class CommitError(UnexpectedError):
    pass


class FlushError(UnexpectedError):
    pass


class RepoError(UnexpectedError):
    pass
