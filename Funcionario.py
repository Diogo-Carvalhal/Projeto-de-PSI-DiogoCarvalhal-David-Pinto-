from Pessoa import pessoa

class funcionario(pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self._salario=salario




   