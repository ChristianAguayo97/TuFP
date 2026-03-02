
from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from app.models.enums import AtributoDestacado
from sqlmodel import Field, SQLModel


if TYPE_CHECKING:
    from app.models.partido import Partido
    from app.models.usuario import Usuario
    
class RendimientoBase(SQLModel):
    id: int 
    promedio_calificaciones: Optional [Decimal] = None
    es_mvp: bool
    atributo_mas_votado: Optional [AtributoDestacado] = None
    votos_mal_partido: int 
    
    delta_atq: Decimal
    delta_def: Decimal
    delta_cre: Decimal
    delta_tec: Decimal
    delta_fis: Decimal
    
    procesado: bool
    
    model_config = {
        "from_attributes": True
    }

class RendimientoPartido(RendimientoBase, table=True):
    __tablename__ = "rendimiento_partido"

    id: Optional[int] = Field(default=None, primary_key=True)
    id_usuario: int = Field(foreign_key="usuario.id", primary_key=True)
    id_partido: int = Field(foreign_key="partido.id", primary_key=True)

    promedio_calificaciones: Optional [Decimal] = Field(default=None, max_digits=4, decimal_places=2)
    es_mvp: bool = Field(default=False)
    atributo_mas_votado: Optional [AtributoDestacado] = Field(default=None)
    votos_mal_partido: int = Field(default=0)
    
    delta_atq: Decimal = Field(default=Decimal("0.0000"), max_digits=5, decimal_places=4)
    delta_def: Decimal = Field(default=Decimal("0.0000"), max_digits=5, decimal_places=4)
    delta_cre: Decimal = Field(default=Decimal("0.0000"), max_digits=5, decimal_places=4)
    delta_tec: Decimal = Field(default=Decimal("0.0000"), max_digits=5, decimal_places=4)
    delta_fis: Decimal = Field(default=Decimal("0.0000"), max_digits=5, decimal_places=4)

    procesado: bool = Field(default=False)