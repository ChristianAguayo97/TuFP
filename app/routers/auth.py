from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import  OAuth2PasswordRequestForm
from sqlmodel import select
from app.routers.deps.db_sessions import SessionDep, UsuarioActual
from app.models.estadistica_usuario import EstadisticaUsuario, CrearEstadistica, MostrarEstadistica
from app.models.usuario import CrearUsuario, MostrarUsuario, Usuario
from app.models.enums import Titulo
from app.core.seguridad import ( obtener_contraseña_hash, verificar_contraseña, crear_token_acceso, ACCESS_TOKEN_EXPIRE_MINUTES)


seguridad_router = APIRouter (prefix="/auth", tags=["Autenticación"])

@seguridad_router.post("/registro", response_model=MostrarUsuario)
def registrar_usuario(usuario: CrearUsuario, db: SessionDep):
    ya_existe = db.exec(
        select(Usuario).where(
            (Usuario.username == usuario.username) | (Usuario.email == usuario.email)
        )
    ).first()
    
    if ya_existe:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username o Email ya existen")
   
    contrasena_hashed = obtener_contraseña_hash(usuario.contrasena)
    
    nuevo_usuario = Usuario(
        nombre= usuario.nombre,
        apellido= usuario.apellido,
        email= usuario.email,
        username= usuario.username,
        foto_perfil = usuario.foto_perfil,
        contrasena = contrasena_hashed
    ) 
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    nueva_estadistica = EstadisticaUsuario(id_usuario=nuevo_usuario.id)
    db.add(nueva_estadistica)
    db.commit()
    db.refresh(nueva_estadistica)
    
    return nuevo_usuario

@seguridad_router.post("/token")
def iniciar_sesion(
    db: SessionDep,
    form_data: OAuth2PasswordRequestForm = Depends(),
    response: Response = None):
    usuario = db.exec(
        select(Usuario).where(
            (Usuario.username == form_data.username) | (Usuario.email == form_data.username)
        )
    ).first()
    if not usuario or not verificar_contraseña(form_data.password, usuario.contrasena):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario o contraseña incorrectos",headers={"WWW-Authenticate": "Bearer"},)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crear_token_acceso(
        data={"sub": usuario.username}, tiempo_expiracion=access_token_expires
    )
    response.set_cookie(key="access_token", value=access_token, httponly=True, samesite="lax")
    return {"access_token": access_token, "token_type": "bearer"}
    
@seguridad_router.post("/completar-estadisticas", response_model=MostrarEstadistica)
def completar_estadisticas(datos: CrearEstadistica, db: SessionDep, usuario_actual: UsuarioActual):
    
    estadistica = db.exec(
        select(EstadisticaUsuario).where(EstadisticaUsuario.id_usuario == usuario_actual.id)
    ).first()
    
    if not estadistica:
        raise HTTPException(status_code=404, detail="Estadísticas no encontradas")

    stats = [datos.ataque, datos.defensa, datos.creacion, datos.tecnica, datos.fisico]
    if sum(stats) != 18:
        raise HTTPException(status_code=400, detail="La suma de estadísticas debe ser exactamente 18")
    
    if any(s == 5 for s in stats):
        if not any(s <= 2 for s in stats):
            raise HTTPException(status_code=400, detail="Si una stat vale 5, al menos otra debe ser 2 o menos")
    
    estadistica.ataque = datos.ataque
    estadistica.defensa = datos.defensa
    estadistica.creacion = datos.creacion
    estadistica.tecnica = datos.tecnica
    estadistica.fisico = datos.fisico
    estadistica.stats_completadas = True
    db.add(estadistica)
    db.commit()
    db.refresh(estadistica)


    titulo = asignar_titulo(datos)
    usuario_actual.titulo = titulo.value
    db.add(usuario_actual)
    db.commit()

    return estadistica


def asignar_titulo(stats: CrearEstadistica) -> Titulo:
    atq = stats.ataque
    def_ = stats.defensa
    cre = stats.creacion
    tec = stats.tecnica
    fis = stats.fisico
    valores = [atq, def_, cre, tec, fis]
    
    if any(s == 1 for s in valores):
        return Titulo.cono_de_entrenamiento
    
    if atq == 5: return Titulo.killer_del_area
    if def_ == 5: return Titulo.cerrojo
    if cre == 5: return Titulo.playmaker
    if tec == 5: return Titulo.malabarista
    if fis == 5: return Titulo.pulmon_de_acero
    
    if atq + tec >= 8: return Titulo.jugador_de_fantasia
    if cre + tec >= 8: return Titulo.director_de_orquesta
    if def_ + fis >= 8: return Titulo.destructor
    if cre + fis >= 8: return Titulo.box_to_box
    if def_ + cre >= 8: return Titulo.lider_tactico
    
    if any(s == 2 for s in valores):
        return Titulo.con_potencial
    
    if max(valores) - min(valores) <= 1:
        return Titulo.hombre_de_equipo
    
    return Titulo.todoterreno
    

    
    
        
        





    