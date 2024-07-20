from animalExotico.animal_exotico import Animal_Exotico

class BoaConstrictor(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratones_comidos = 0

    def hacer_sonido(self) -> str:
        return "¡Tsss!"

    def agregar_raton(self):
        self.__ratones_comidos += 1

    def get_ratones_comidos(self) -> int:
        return self.__ratones_comidos
