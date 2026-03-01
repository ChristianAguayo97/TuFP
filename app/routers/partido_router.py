from app.models.partido import MostrarPartido, CrearPartido, Partido
from app.models.partido_usuario import PartidoUsuario
from fastapi import APIRouter


partido_router = APIRouter(
    prefix="/partido",
    tags=["partido"])

partido_usuario_router = APIRouter(
    prefix="/partido_usuario",
    tags=["partido_usuario"])

