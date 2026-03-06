from fastapi import APIRouter
from app.models.enums import EstadoPartido
from app.models.partido import Partido, MostrarPartido, CrearPartido, PartidoUsuario
from app.models.usuario import Usuario
from app.routers.deps.db_sessions import SessionDep, UsuarioActual
from sqlmodel import select
from fastapi import HTTPException
import uuid
from app.models.invitacion import Invitacion
from app.models.cancha import Cancha



partido_router = APIRouter (prefix="/partidos", tags=["Partidos"])


@partido_router.post("/crear", response_model=MostrarPartido)
def crear_partido(datos: CrearPartido, db: SessionDep, usuario_actual: UsuarioActual):
    cancha = db.exec(select(Cancha).where(Cancha.id == datos.id_cancha)).first()
    if not cancha:
        raise HTTPException(status_code=404, detail="Cancha no encontrada")
    jugadores_minimos = int(cancha.tipo_cancha.value) * 2
    link = str(uuid.uuid4())
    nuevo_partido = Partido(
        id_creadorPartido=usuario_actual.id,
        id_cancha=datos.id_cancha,
        horario=datos.horario,
        link_compartir=link,
        jugadores_minimos=jugadores_minimos,
    )
    db.add(nuevo_partido)
    db.commit()
    db.refresh(nuevo_partido)
    nuevo_partido.jugadores.append(usuario_actual)
    db.commit()
    for username in datos.usuarios_invitados:
        usuario = db.exec(select(Usuario).where(Usuario.username == username)).first()
        if not usuario:
            raise HTTPException(status_code=404, detail=f"Usuario '{username}' no encontrado")
        invitacion = Invitacion(
            id_partido=nuevo_partido.id,
            id_usuario=usuario.id
        )
        db.add(invitacion)
    db.commit()
    db.refresh(nuevo_partido)

    return MostrarPartido.from_partido(nuevo_partido)

@partido_router.get("/{id_partido}", response_model=MostrarPartido)  # ← sacás List[]
def obtener_partido(id_partido: int, db: SessionDep):
    partido = db.exec(select(Partido).where(Partido.id == id_partido)).first()
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    return MostrarPartido.from_partido(partido).model_dump()

@partido_router.post("/unirse/{link}", response_model=MostrarPartido)
def unirse_por_link(link: str, db: SessionDep, usuario_actual: UsuarioActual):
    partido = db.exec(select(Partido).where(Partido.link_compartir == link)).first()
    if not partido:
        raise HTTPException (status_code=404, detail="Link Invalido")
    if partido.estado != EstadoPartido.abierto:
        raise HTTPException (status_code=400, detail= "El partido no está disponible")
    registrado = db.exec(select(PartidoUsuario).where(
        PartidoUsuario.id_partido == partido.id,
        PartidoUsuario.id_usuario == usuario_actual
        )).first()
    if registrado:
        raise HTTPException(status_code=400, detail="Ya esta registrado en el partido")
    
    partido.jugadores.append(usuario_actual)
    db.commit()
    db.refresh(partido)
    return MostrarPartido.from_partido(partido).model_dump