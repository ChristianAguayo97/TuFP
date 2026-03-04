from typing import TYPE_CHECKING, List, Optional
from pydantic import model_validator
from sqlmodel import Field, Relationship, SQLModel
from app.models.enums import EstadoPartido
from app.models.partido_usuario import PartidoUsuario
from datetime import datetime, timezone



if TYPE_CHECKING:
    from app.models.usuario import Usuario
    from app.models.cancha import Cancha
    from app.models.equipo import Equipo
    from app.models.resultado import Resultado
    
class PartidoBase(SQLModel):
    horario: datetime 
    model_config = {
        "from_attributes": True
    }
    
class CrearPartido(PartidoBase):
    id_cancha: int
    usuarios_invitados: List [str] = []
    
class MostrarJugadorAceptado(SQLModel):
    id: int
    username: str
    foto_perfil: Optional[str] = None

    model_config = {
        "from_attributes": True
    }

class MostrarPartido(PartidoBase):
    id: int
    estado: EstadoPartido
    link_compartir: str
    jugadores_minimos: int
    equipos_generados: bool
    created_at: datetime
    jugadores_aceptados: List[MostrarJugadorAceptado] = []

    model_config = {
        "from_attributes": True
    }

    @classmethod
    def from_partido(cls, partido: "Partido") -> "MostrarPartido":
        return cls(
            horario=partido.horario,
            id=partido.id,
            estado=partido.estado,
            link_compartir=partido.link_compartir,
            jugadores_minimos=partido.jugadores_minimos,
            equipos_generados=partido.equipos_generados,
            created_at=partido.created_at,
            jugadores_aceptados=partido.jugadores
        )


class Partido(PartidoBase, table=True):
    __tablename__ = "partido"
    id: Optional[int] = Field(default=None, primary_key=True)
    id_creadorPartido: int = Field(foreign_key="usuario.id", nullable=False)
    id_cancha: int = Field(foreign_key="cancha.id", nullable=False)
    estado: EstadoPartido = Field(default= EstadoPartido.abierto, nullable=False)
    link_compartir: str = Field(max_length=255, unique= True, nullable=False)
    jugadores_minimos: int = Field(nullable=False)
    equipos_generados: bool = Field(default=False)
    
    jugadores: List ["Usuario"] = Relationship(back_populates="partido", link_model=PartidoUsuario)
    equipos: List ["Equipo"] = Relationship(back_populates="partido")
    cancha: Optional["Cancha"] = Relationship(back_populates="partidos")
    creador: Optional["Usuario"] = Relationship()
    resultado: Optional["Resultado"] = Relationship(back_populates="partido")
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)

    
    
    