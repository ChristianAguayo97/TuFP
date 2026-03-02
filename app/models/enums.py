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
    # Hibridos
    jugador_de_fantasia  = "jugador_de_fantasia"
    director_de_orquesta = "director_de_orquesta"
    destructor           = "destructor"
    box_to_box           = "box_to_box"
    lider_tactico        = "lider_tactico"
    # Otros
    todoterreno = "todoterreno"
    promesa     = "promesa"

    def label(self) -> str:
        """Devuelve el nombre legible para mostrar en la UI."""
        labels = {
            "killer_del_area":     "Killer del Area",
            "cerrojo":             "Cerrojo",
            "playmaker":           "Playmaker",
            "malabarista":         "Malabarista",
            "pulmon_de_acero":     "Pulmon de Acero",
            "jugador_de_fantasia": "Jugador de Fantasia",
            "director_de_orquesta":"Director de Orquesta",
            "destructor":          "Destructor",
            "box_to_box":          "Box-to-Box",
            "lider_tactico":       "Lider Tactico",
            "todoterreno":         "Todoterreno",
            "promesa":             "Promesa",
        }
        return labels[self.value]