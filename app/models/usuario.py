from datetime import datetime, timezone
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, SQLModel, Relationship
from app.models.partido_usuario import PartidoUsuario
from app.models.equipo_usuario import EquipoUsuario
from app.models.estadistica_usuario import EstadisticaUsuario, MostrarEstadistica, EstadisticaBase

if TYPE_CHECKING: 
    from app.models.partido import Partido
    from app.models.invitacion import Invitacion
    from app.models.equipo import Equipo
    from app.models.resultado import Resultado



class UsuarioBase(SQLModel):
    nombre: str
    apellido: str
    email: str = Field(unique=True, index=True, max_length=255, nullable=False)
    username: str = Field (unique=True, index=True, max_length=30, nullable=False)
    foto_perfil: Optional[str] = Field(default=None)
    
class CrearUsuario(UsuarioBase):
    contrasena: str

class LoginUsuario(SQLModel):
    username_o_email: str
    contrasena: str

class ActualizarUsuario(SQLModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    foto_perfil_url: Optional[str] = None
    username: Optional[str] = None
    contrasena: Optional[str] = None


class MostrarUsuario(UsuarioBase):
    id: int
    titulo: Optional[str] = None
    partidos_ganados: int
    partidos_perdidos: int
    partidos_empatados: int
    created_at: datetime
    estadisticas: Optional[MostrarEstadistica] = None
    model_config = {
        "from_attributes": True
    }
    
class MostrarUsuarioSimple(SQLModel):
    id: int
    username: str
    foto_perfil: Optional[str] = None
    titulo: Optional[str] = None
    partidos_ganados: int
    partidos_perdidos: int
    partidos_empatados: int
    estadisticas: Optional[EstadisticaBase] = None
    model_config = {
        "from_attributes": True
    }  

class Usuario(UsuarioBase, table=True):
    __tablename__ = "usuario"
    id: Optional[int] = Field(default=None, primary_key=True)
    contrasena: str = Field(nullable=False)
    titulo: Optional[str] = Field(default=None )
    partidos_ganados: int = Field(default=0)
    partidos_perdidos: int = Field(default=0)
    partidos_empatados: int = Field(default=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    resultados_ingresados: List["Resultado"] = Relationship(back_populates="ingresado_por_usuario")
    
    partido: List ["Partido"] = Relationship(back_populates="jugadores", link_model= PartidoUsuario)
    equipo: List ["Equipo"] = Relationship(back_populates="jugadores_equipo", link_model=EquipoUsuario)

    invitaciones: List ["Invitacion"] = Relationship(back_populates="usuario")
    estadisticas: Optional["EstadisticaUsuario"] = Relationship(back_populates="usuario")