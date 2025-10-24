from Pessoa import pessoa

class Gerente(pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
        self.bonus = salario 

    def mostrar_informacoes(self):
        print(f"Gerente: {self.nome}, Idade: {self.idade}, "
              f"Salário: {self.salario:.2f}, Bônus: {self.bonus:.2f}")

    def gerar_relatorio(self, funcionarios):
        print("\n--- Relatório de Funcionários ---")
        for f in funcionarios:
            f.mostrar_informacoes()