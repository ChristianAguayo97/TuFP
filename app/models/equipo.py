from decimal import Decimal
from typing import TYPE_CHECKING, List, Optional
from app.models.enums import NombreEquipo
from app.models.equipo_usuario import EquipoUsuario
from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from app.models.usuario import Usuario
    from app.models.partido import Partido


class EquipoBase(SQLModel):
    id_partido: int
    nombre_equipo: NombreEquipo


class MostrarJugadorEnEquipo(SQLModel):
    id: int
    username: str
    foto_perfil: Optional[str] = None
    model_config = {
        "from_attributes": True
    }
    
    
class MostrarEquipo(SQLModel):
    id: int
    rating_promedio: Decimal
    promedio_ataque: Decimal
    promedio_defensa: Decimal
    jugadores: List[MostrarJugadorEnEquipo] = []
    model_config = {
        "from_attributes": True
    }

class Equipo(EquipoBase, table=True):
    __tablename__ = "equipo"
    id: Optional[int] = Field(default=None, primary_key=True)
    id_partido: int = Field(foreign_key="partido.id", nullable=False)
    nombre_equipo: NombreEquipo = Field( nullable=False)
    jugadores_equipo: List["Usuario"] = Relationship(back_populates="equipo", link_model=EquipoUsuario)
    rating_promedio: Decimal = Field(default=Decimal("0.00"), max_digits=5, decimal_places=2)
    promedio_ataque: Decimal = Field(default=Decimal("0.00"), max_digits=4, decimal_places=2)
    promedio_defensa: Decimal = Field(default=Decimal("0.00"), max_digits=4, decimal_places=2)
    partido: Optional["Partido"] = Relationship(back_populates="equipos")



    
