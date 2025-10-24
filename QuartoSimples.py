from Quarto import quarto

class Quarto_simples(quarto):
    def __init__(self, Nquarto_simples, Preco_Diario, ID_Quarto_simples):
        super().__init__(Preco_Diario)
        self._ID_Quarto_simples=ID_Quarto_simples
        self._Nquarto_simples=Nquarto_simples

    @property
    def Ocupado(self):
       pass 

    @property
    def Preco_Diario(self):
        return self._Preco_Diario
    
    @Preco_Diario.setter
    def Preco_Diario(self, Preco):
        if Preco < 0:
            print("O preco diario nao pode ser negativo!!")
        self.Preco_Diario=Preco

    def mostrar_informacoes(self):
        print(f"Preço do quarto: {self.Preco_Diario:.2f}, Turno: {self._ID_Quarto_luxo}, "
              f"Salário: {self._Nquarto_simples}")