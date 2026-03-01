from typing import TYPE_CHECKING, List, Optional
from app.models.enums import Tipo_cancha
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.partido import Partido


class CanchaBase(SQLModel):
    nombre: str = Field (max_length=100, nullable=False)
    direccion: Optional[str] = Field(default=None)
    tipo_cancha: Tipo_cancha = Field(default=None)
    

class MostrarCancha(CanchaBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class Cancha(CanchaBase, table=True):
    __tablename__ = "cancha"
    id: Optional[int] = Field(default=None, primary_key=True)
    partidos: List["Partido"] = Relationship(back_populates="cancha")