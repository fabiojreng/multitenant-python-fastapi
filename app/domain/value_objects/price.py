class Price:
    def __init__(self, value: float) -> None:
        if value < 0:
            raise ValueError("O valor não pode ser negativo")
        self.__value = value

    def get_value(self) -> float:
        return self.__value
