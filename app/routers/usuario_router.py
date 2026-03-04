from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.models.usuario import MostrarUsuario, Usuario, MostrarUsuarioSimple,ActualizarUsuario
from app.core.seguridad import obtener_contraseña_hash
from app.routers.deps.db_sessions import SessionDep, UsuarioActual


usuario_router = APIRouter (prefix="/usuario", tags=["Usuario"])

@usuario_router.get("/usuario-logueado", response_model=MostrarUsuario)
def obtener_usuario_logueado(usuario_actual: UsuarioActual):
    return usuario_actual

@usuario_router.get("/buscar_usuario", response_model=MostrarUsuarioSimple)
def buscar_usuario(username: str, db: SessionDep):
    usuario = db.exec(
        select(Usuario).where(Usuario.username == username)
    ).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@usuario_router.patch("/actualizar-usuario", response_model=MostrarUsuario)
def actualizar_usuario(datos: ActualizarUsuario, db: SessionDep, usuario_actual: UsuarioActual):
    if datos.nombre is not None:
        usuario_actual.nombre = datos.nombre
    if datos.apellido is not None:
        usuario_actual.apellido = datos.apellido
    if datos.username is not None:
        existe = db.exec(select(Usuario).where(Usuario.username == datos.username)).first()
        if existe:
            raise HTTPException(status_code=400, detail="Ese username ya está en uso")
        usuario_actual.username = datos.username
    if datos.foto_perfil_url is not None:
        usuario_actual.foto_perfil = datos.foto_perfil_url
    if datos.contrasena is not None:
        usuario_actual.contrasena = obtener_contraseña_hash(datos.contrasena)
    db.add(usuario_actual)
    db.commit()
    db.refresh(usuario_actual)
    return usuario_actual