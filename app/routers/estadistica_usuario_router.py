from app.models.estadistica_usuario import CrearEstadistica, MostrarEstadistica, EstadisticaUsuario
from fastapi import APIRouter


estadistica_router = APIRouter(
    prefix="/estadistica",
    tags=["estadistica"])