from sqlmodel import SQLModel
from fastapi import FastAPI
from app.config.db import engine
from app import models
from fastapi.middleware.cors import CORSMiddleware
from app.routers.auth import seguridad_router
from app.routers.usuario_router import usuario_router
from app.routers.cancha_router import canchas_router
from app.routers.partido_router import partido_router





SQLModel.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción pondrías la URL de tu front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(seguridad_router)
app.include_router(usuario_router)
app.include_router(canchas_router)
app.include_router(partido_router)



@app.get("/")
def home():
    return 'Bienvenido a la API de TuFP!'

