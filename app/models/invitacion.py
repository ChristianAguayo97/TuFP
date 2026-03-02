from datetime import datetime, timezone
from app.models.enums import EstadoInvitacion
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from app.models.partido import Partido
    from app.models.usuario import Usuario


class InvitacionBase(SQLModel):
    id_partido: int
    id_usuario: int
    
class MostrarInvitacion(InvitacionBase):
    id: int
    id_partido: int
    estado: EstadoInvitacion
    via_link: bool
    create_at: datetime
    model_config = {
        "from_attributes": True
    }

class ResponderInvitacion():
    estado: EstadoInvitacion
    
class Invitacion(InvitacionBase, table=True):
    __tablename__ = "invitacion"
    id: int= Field(default=None, primary_key=True)
    id_partido: int = Field(foreign_key="partido.id", nullable=False)
    id_usuario: int = Field(foreign_key="usuario.id", nullable=False)
    estado: EstadoInvitacion = Field(default=EstadoInvitacion.pendiente, nullable=False)
    usuario: Optional["Usuario"] = Relationship(back_populates="invitaciones")
    via_link: bool = Field(default=False, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    

