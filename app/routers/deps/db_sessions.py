from typing import Annotated, Generator
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from app.config.db import engine
from app.core.seguridad import obtener_usuario_actual
from app.models.usuario import Usuario



def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        
SessionDep = Annotated[Session, Depends(get_db)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: SessionDep) -> Usuario:
    return obtener_usuario_actual(token, db)

UsuarioActual = Annotated[Usuario, Depends(get_current_user)]