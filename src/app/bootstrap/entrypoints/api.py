from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

from app.presentation.api.root import root_router


def init_routers(app: FastAPI) -> None:
    app.include_router(root_router)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    yield


def create_app() -> FastAPI:
    load_dotenv()
    app = FastAPI(lifespan=lifespan)
    init_routers(app)
    return app
