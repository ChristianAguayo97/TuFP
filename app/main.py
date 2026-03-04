from sqlmodel import SQLModel
from fastapi import FastAPI
from app.config.db import engine
from app import models
from app.routers.auth import seguridad_router


SQLModel.metadata.create_all(engine)

app = FastAPI()

app.include_router(seguridad_router)


@app.get("/")
def home():
    return 'Bienvenido a la API de TuFP!'

