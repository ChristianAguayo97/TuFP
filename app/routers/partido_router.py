from app.models.partido import MostrarPartido, CrearPartido, Partido
from app.models.partido_usuario import PartidoUsuario
from app.models.invitacion import Invitacion, MostrarInvitacion, ReponderInvitacion
from fastapi import APIRouter


partido_router = APIRouter(
    prefix="/partido",
    tags=["partido"])

partido_usuario_router = APIRouter(
    prefix="/partido_usuario",
    tags=["partido_usuario"])

invitacion_router = APIRouter(
    prefix="/invitacion",
    tags=["invitacion"])


