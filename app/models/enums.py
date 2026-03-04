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

class EstadoConfirmacion(str, Enum):
    pendiente = "pendiente"
    confirmado = "confirmado"
    auto_aprobado = "auto_aprobado"

class AtributoDestacado(str, Enum):
    ATQ = "ATQ"
    DEF = "DEF"
    CRE = "CRE"
    TEC = "TEC"
    FIS = "FIS"
    MAL = "MAL" 

class Titulo(str, Enum):
    # Especialistas
    killer_del_area    = "killer_del_area"
    cerrojo            = "cerrojo"
    playmaker          = "playmaker"
    malabarista        = "malabarista"
    pulmon_de_acero    = "pulmon_de_acero"
    # Híbridos
    jugador_de_fantasia  = "jugador_de_fantasia"
    director_de_orquesta = "director_de_orquesta"
    destructor           = "destructor"
    box_to_box           = "box_to_box"
    lider_tactico        = "lider_tactico"
    # Equilibrados
    todoterreno      = "todoterreno"
    hombre_de_equipo = "hombre_de_equipo"
    # En desarrollo
    con_potencial = "malo pero no tan malo"
    # Malos
    cono_de_entrenamiento = "cono_de_entrenamiento"