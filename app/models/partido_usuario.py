from typing import Optional
from sqlmodel import Field, SQLModel


class PartidoUsuario(SQLModel, table=True):
    id_partido: Optional[int] = Field(default=None, foreign_key="partido.id", primary_key=True)
    id_usuario: Optional[int] = Field(default=None, foreign_key="usuario.id", primary_key=True)