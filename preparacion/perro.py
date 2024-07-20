from .animal import Animal

class Perro(Animal):
    def __init__(self, nombre: str, raza: str, peso: float, edad: int):
        super().__init__(nombre, peso, edad)
        self.__raza = raza

    def hacer_sonido(self) -> str:
        return "¡Guau, guau!"
    
    def get_raza (self) -> str:
        return self.__raza
    