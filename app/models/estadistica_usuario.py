from datetime import datetime, timezone
from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.usuario import Usuario


class EstadisticaBase(SQLModel):
    ataque: Decimal = Field(default=Decimal("0.00"), max_digits=4, decimal_places=2)
    defensa: Decimal = Field(default=Decimal("0.00"), max_digits=4, decimal_places=2)
    creacion: Decimal = Field(default=Decimal("0.00"), max_digits=4, decimal_places=2)
    tecnica: Decimal = Field(default=Decimal("0.00"), max_digits=4, decimal_places=2)
    fisico: Decimal = Field(default=Decimal("0.00"), max_digits=4, decimal_places=2)

class CrearEstadistica(EstadisticaBase):
    ataque: int = Field(ge=1, le=5)
    defensa: int = Field(ge=1, le=5)
    creacion: int = Field(ge=1, le=5)
    tecnica: int = Field(ge=1, le=5)
    fisico: int = Field(ge=1, le=5)

class MostrarEstadistica(EstadisticaBase):
    id: int
    id_usuario: int
    rating_total: Decimal
    stats_completadas: bool
    update_at: datetime 
    model_config = {
        "from_attributes": True
    }


class EstadisticaUsuario(EstadisticaBase, table = True):
    __tablename__ = "estadistica_usuario"
    __table_args__ = (UniqueConstraint("id_usuario", name="uq_estadistica_usuario"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    id_usuario: int = Field(foreign_key="usuario.id", nullable=False)
    
    ataque_xp: Decimal = Field(default=Decimal("0.0000"), max_digits=6, decimal_places=4)
    defensa_xp: Decimal = Field(default=Decimal("0.0000"), max_digits=6, decimal_places=4)
    creacion_xp: Decimal = Field(default=Decimal("0.0000"), max_digits=6, decimal_places=4)
    tecnica_xp: Decimal = Field(default=Decimal("0.0000"), max_digits=6, decimal_places=4)
    fisico_xp: Decimal  = Field(default=Decimal("0.0000"), max_digits=6, decimal_places=4)
    
    rating_total: Decimal = Field(default=Decimal("0.0000"), max_digits=5, decimal_places=2)
    update_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    stats_completadas: bool = Field(default=False, nullable=False)
    
    usuario: Optional["Usuario"] = Relationship(back_populates="estadisticas")
    
    
