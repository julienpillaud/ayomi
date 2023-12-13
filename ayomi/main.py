from fastapi import FastAPI

from ayomi.routers import rpn

app = FastAPI()

app.include_router(rpn.router)
