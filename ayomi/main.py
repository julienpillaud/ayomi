from fastapi import FastAPI

from ayomi.routers import rpn

app = FastAPI(title="Ayomi")

app.include_router(rpn.router)
