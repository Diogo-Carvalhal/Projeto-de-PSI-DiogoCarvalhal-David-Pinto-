from Funcionario import funcionario

class recepcionista(funcionario):
    def __init__(self, nome, id_func, idade, salario, turno):
        super().__init__(nome, idade, salario)
        self.id_func = id_func
        self.salario = salario
        self.turno = turno

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, valor):
        if valor not in ["manha", "tarde", "noite"]:
            raise ValueError("Turno inválido.")
        self._turno = valor

    def mostrar_informacoes(self):
        print(f"Recepcionista: {self.nome}, Turno: {self.turno}, "
              f"Salário: {self.salario:.2f}")