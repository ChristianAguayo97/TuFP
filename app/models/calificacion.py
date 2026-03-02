from datetime import datetime, timezone
from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, SQLModel
from app.models.enums import AtributoDestacado



if TYPE_CHECKING:
    from app.models.partido import Partido
    from app.models.usuario import Usuario


class CalificacionBase(SQLModel):
    id_partido: int
    id_calificado: int
    
class EmitirCalificacion(CalificacionBase):
    puntaje_generel: int = Field(ge=1, le=10)
    atributo_destacado: AtributoDestacado
    es_mvp_voto: bool = False

class MostrarCalificacion(CalificacionBase):
    id: int
    id_votante: int
    puntaje_general: int
    atributo_destacado: AtributoDestacado
    es_mvp_voto: bool 
    es_rival: bool
    created_at: datetime
    model_config = {
        "from_attributes": True
    }

class Calificacion(CalificacionBase, table=True):
    __tablename__ = "calificacion"
    id: Optional[int] = Field(default=None, primary_key=True)
    id_partido: int = Field(foreign_key="partido.id", nullable=False)
    id_votante: int = Field(foreign_key="usuario.id", nullable=False)
    id_calificado: int = Field(foreign_key="usuario.id", nullable=False)

    puntaje_general: int = Field(ge=1, le=10, nullable=False)
    atributo_destacado: AtributoDestacado = Field(nullable=False)
    es_mvp_voto: bool = Field(default=False)
    
    peso_voto: Decimal = Field(default=Decimal("1.000"), max_digits=4, decimal_places=3)
    es_rival: bool = Field(default=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    
    

    