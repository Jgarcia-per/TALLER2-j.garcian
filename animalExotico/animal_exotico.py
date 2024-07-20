from preparacion.animal import Animal

class Animal_Exotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad)
        self.__pais_origen = pais_origen
        self.__impuestos = impuestos

    def calcular_flete(self) -> float:
        return self.__impuestos * self.get_peso()

    def get_pais_origen(self) -> str:
        return self.__pais_origen

    def get_impuestos(self) -> float:
        return self.__impuestos
