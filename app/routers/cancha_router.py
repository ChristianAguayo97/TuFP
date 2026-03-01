from fastapi import APIRouter
from app.models.cancha import MostrarCancha, Cancha

cancha_router = APIRouter(
    prefix="/cancha",
    tags=["cancha"])


