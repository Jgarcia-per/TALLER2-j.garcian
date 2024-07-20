from .ianimal import iAnimal

class Animal(iAnimal):
    def __init__(self, nombre: str, peso: float, edad: int):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos=0

    def comer(self, kilos):
        self._kilos_comidos += kilos

    def get_kilos_comidos(self):
        return self._kilos_comidos

    def hacer_sonido(self):
        pass

    def get_nombre(self):
        return self._nombre
    
    def get_peso(self):
        return self._peso
    
    def get_edad(self):
        return self._edad