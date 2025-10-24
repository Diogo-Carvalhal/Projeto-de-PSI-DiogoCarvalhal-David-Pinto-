from abc import ABC, abstractmethod

class pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade


    @property
    @abstractmethod
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, novo_nome):
        pass

    @property
    @abstractmethod
    def idade(self):
        pass

    @idade.setter
    @abstractmethod
    def idade(self, nova_idade):
        pass

    @abstractmethod
    def mostrar_informacoes(self):
        pass

    