from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ayomi.database import init_db
from ayomi.routers import rpn


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:  # noqa
    init_db()
    yield


app = FastAPI(title="Ayomi", lifespan=lifespan)

app.include_router(rpn.router)
