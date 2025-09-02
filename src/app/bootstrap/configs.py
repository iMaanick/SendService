from dataclasses import dataclass
from os import environ


@dataclass
class MissingDatabaseConfigError(ValueError):

    @property
    def title(self) -> str:
        return "Required db environment variables are missing"


@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    db_name: str
    user: str
    port: int
    password: str

    @property
    def uri(self) -> str:
        return (
            f"postgresql+psycopg://{self.user}:{self.password}@{self.host}"
            f":{self.port}/{self.db_name}"
        )


def load_database_config() -> DatabaseConfig:
    host = environ.get("DB_HOST")
    port = environ.get("POSTGRES_PORT")
    db_name = environ.get("POSTGRES_DB")
    user = environ.get("POSTGRES_USER")
    password = environ.get("POSTGRES_PASSWORD")

    if (
            host is None
            or port is None
            or db_name is None
            or user is None
            or password is None
    ):
        raise MissingDatabaseConfigError

    return DatabaseConfig(
        host=host,
        port=int(port),
        db_name=db_name,
        user=user,
        password=password,
    )
