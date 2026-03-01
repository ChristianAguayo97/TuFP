from sqlmodel import SQLModel
from fastapi import FastAPI
from app.routers.cancha_router import cancha_router
from app.routers.usuario_router import usuario_router, estadistica_router
from app.routers.partido_router import partido_router, partido_usuario_router
from app.config.db import engine



SQLModel.metadata.create_all(engine)

app = FastAPI()

app.include_router(cancha_router)
app.include_router(usuario_router)
app.include_router(estadistica_router)
app.include_router(partido_router)
app.include_router(partido_usuario_router)

@app.get("/")
def home():
    return 'Bienvenido a la API de Tareas!'

