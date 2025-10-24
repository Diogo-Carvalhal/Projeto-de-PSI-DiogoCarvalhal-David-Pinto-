from Recepcionista import recepcionista
from TecnicoManutencao import tecnico_manutencao


class tecnico_recepcao(recepcionista, tecnico_manutencao):
    def __init__(self, nome, id_func, idade, salario, turno, especialidade, reparo):
        recepcionista().__init__(nome, id_func, idade, salario, turno)
        tecnico_manutencao().__init__(nome, idade, salario, especialidade)
        self._reparo=[]

    def registrar_reparo(self, descricao):
        self._reparo.append(descricao)
        print(f"Reparo registrado: {descricao}")


    def mostrar_informacoes(self):
        if not self._reparo:
            print("não existe nenhum reparo feito")



        