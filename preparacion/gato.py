from .animal import Animal

class Gato(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, color: str):
        super().__init__(nombre, peso, edad)
        self.__color = color


    def hacer_sonido(self) -> str:
        return "¡Miau, miau!"
    
    def get_color (self) -> str:
        return self.__color