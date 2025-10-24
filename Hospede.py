from Pessoa import pessoa

class hospede(pessoa):
    def __init__ (self, nome, idade, dias_estadia):
        super().__init__(nome, idade)
        self.dias_estadia = dias_estadia

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        self._idade = nova_idade

    def mostrar_informacoes(self):
        print(f"Preço do quarto: {self._nome}, Turno: {self._idade}, "
              f"Salário: {self._Nquarto}")
        


