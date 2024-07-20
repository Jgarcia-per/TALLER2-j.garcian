from abc import ABC, abstractmethod

class iAnimal(ABC):
    @abstractmethod
    def comer(self, kilos):
        pass

    @abstractmethod
    def get_kilos_comidos(self):
        pass