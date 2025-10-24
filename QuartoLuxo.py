from Quarto import quarto

class quarto_luxo(quarto):
    def __init__(self, Nquarto_luxo, Preco_Diario, ID_Quarto_luxo):
        super().__init__(Preco_Diario)
        self._ID_Quarto_luxo=ID_Quarto_luxo
        self._Nquarto_luxo=Nquarto_luxo
    


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
              f"Salário: {self._Nquarto_luxo}")