from app.models.equipo import MostrarEquipo, Equipo
from fastapi import APIRouter


equipos_router= APIRouter(
    prefix="/equipos",
    tags=["equipos"])