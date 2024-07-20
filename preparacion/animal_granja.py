from .ianimal import iAnimal

class Animal_Granja(iAnimal):
    def __init__(self, nombre, pseo, edad):
        self._kilos_comidos=0

    def comer(self, kilos):
        self._kilos_comidos += (kilos*0.8)

    def get_kilos_comidos(self):
        return self._kilos_comidos