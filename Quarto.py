from abc import ABC, abstractmethod


class quarto(ABC):
    def __init__(self, Preco_Diario):
        self._Preco_Diario=Preco_Diario

    @property
    @abstractmethod
    def Ocupado(self):
        pass

    @property
    @abstractmethod
    def Preco_Diario(self):
        pass

    @Preco_Diario.setter
    @abstractmethod
    def Preco_Diario(self):
        pass

    @abstractmethod
    def mostrar_informacoes():
        pass