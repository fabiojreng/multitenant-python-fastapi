from enum import Enum


class StockMovementType(str, Enum):
    ENTRADA = "in"
    SAIDA = "out"
