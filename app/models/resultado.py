from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional
from app.models.enums import EstadoConfirmacion
from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from app.models.usuario import Usuario
    from app.models.partido import Partido

class ResultadoBase(SQLModel):
    id_partido: int 

class IngresarResultado(SQLModel):
    goles_equipo_a: int = Field (ge=0)
    goles_equipo_b: int = Field (ge=0)

class MostrarResultado(ResultadoBase):
    id: int
    goles_equipo_a: int
    goles_equipo_b: int
    estado_confirmacion: EstadoConfirmacion
    model_config = {
        "from_attributes": True
    }

class Resultado(ResultadoBase, table=True):
    __tablename__ = "resultado"
    id: int = Field(default=None, primary_key=True)
    id_partido: int = Field(foreign_key="partido.id", nullable=False)
    ingresado_por: int = Field(foreign_key="usuario.id", nullable=False)
    goles_equipo_a: int = Field(ge=0, nullable=False)
    goles_equipo_b: int = Field(ge=0, nullable=False)
    estado_confirmacion: EstadoConfirmacion = Field(default=EstadoConfirmacion.pendiente, nullable=False)
    
    fecha_ingreso: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),nullable=False)
    fecha_confirmacion: Optional[datetime] = Field(default=None)
    
    ventana_votos_inicio: Optional[datetime] = Field(default=None)
    ventana_votos_fin: Optional[datetime] = Field(default=None)
    partido: Optional["Partido"] = Relationship(back_populates="resultado")
    ingresado_por_usuario: Optional["Usuario"] = Relationship(back_populates="resultados_ingresados")
    
