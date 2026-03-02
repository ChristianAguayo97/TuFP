from sqlmodel import SQLModel
from fastapi import FastAPI
from app.config.db import engine



SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def home():
    return 'Bienvenido a la API de TuFP!'

