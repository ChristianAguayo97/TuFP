from typing import Optional
from sqlmodel import Field, SQLModel

class EquipoUsuario(SQLModel, table=True):
    __tablename__ = "equipo_usuario"
    id_usuario: Optional[int] = Field(default=None, foreign_key="usuario.id", primary_key=True)
    id_equipo: Optional[int] = Field(default=None, foreign_key="equipo.id", primary_key=True)   