from app.models.usuario import CrearUsuario, LoginUsuario, ActualizarUsuario, MostrarUsuario, Usuario
from app.models.estadistica_usuario import CrearEstaditica, MostrarEstadistica, EstadisticaUsuario
from fastapi import APIRouter


usuario_router = APIRouter(
    prefix="/usuario",
    tags=["usuario"])

estadistica_router = APIRouter(
    prefix="/estadistica",
    tags=["estadistica"])