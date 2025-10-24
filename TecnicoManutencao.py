from Funcionario import funcionario

class tecnico_manutencao(funcionario):
    def __init__(self,nome, idade, salario, especialidade):
        super.__init__(nome, idade, salario)
        self._especialidade=especialidade

    @property
    def especialidade(self):
        return self._especialidade