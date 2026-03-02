from enum import Enum

class Tipo_cancha(str, Enum):
    cinco = "5"
    siete = "7"
    nueve = "9"
    once = "11"

class EstadoPartido(str, Enum):
    abierto = "abierto"
    completo = "completo"
    en_curso = "en curso"
    finalizado = "finalizado"
    cancelado = "cancelado"
    
class NombreEquipo(str, Enum):
    equipo_a = "Equipo A"
    equipo_b = "Equipo B"
    
class EstadoInvitacion(str, Enum):
    aceptada = "aceptada"
    rechazada = "rechazada"
    pendiente = "pendiente"

