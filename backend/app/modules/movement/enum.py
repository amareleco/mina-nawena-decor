from enum import Enum

class MovementType(str, Enum):
    ENTRY = "ENTRADA"
    EXIT = "SAIDA"
    RETURN = "DEVOLUCAO"
    DAMAGED = "DANIFICADO"