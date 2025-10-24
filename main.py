from Hospede import hospede
from QuartoLuxo import quarto_luxo
from QuartoSimples import Quarto_simples
from TecnicoManutencao import tecnico_manutencao
from Recepcionista import recepcionista
from TecnicoRecepcao import tecnico_recepcao

lista_quarto_luxo = []
lista_quarto_simples = []
lista_hospede = []
lista_especialidade = []
lista_recepcionista = []
lista_tecnico_recepcao = []

ID_Quarto_simples = 0
ID_Quarto_luxo = 0
id_func = 0

while True:
    print("1 - Alugar um quarto")
    print("2 - Mostrar informações")
    print("3 - Introduzir as informações dos quartos")
    print("4 - Definir a sua especialidade")
    print("5 - Introduzir as informações do recepcionista")
    print("6 - Escolher o turno que deseja")
    print("7 - Registrar o reparo")
    print("0 - Sair")

    op = input("Escolha uma opção: ")

    match op:
        case "1":
            if not lista_hospede:
                print("Quartos não disponiveis")
            else:
                nome = input("Insira o seu nome: ")
                idade = int(input("Insira a sua idade: "))
                dias_estadia = int(input("Insira os dias que deseja ficar: "))
                H = hospede(nome, idade, dias_estadia)
                lista_hospede.append(H)

            print("\nQual é o quarto que deseja alugar?")
            print("1 - Quarto simples")
            print("2 - Quarto luxo")
            op_quarto = input("Escolha uma opção: ")

            match op_quarto:
                case "1":
                    if not lista_quarto_simples:
                        print("Não existe nenhum quarto simples disponível.")
                    else:
                        quarto = lista_quarto_simples[0]
                        print(f"Quarto simples alugado! Preço diário: {quarto.Preco_Diario}")
                case "2":
                    if not lista_quarto_luxo:
                        print("Não existe nenhum quarto de luxo disponível.")
                    else:
                        quarto = lista_quarto_luxo[0]
                        print(f"Quarto de luxo alugado! Preço diário: {quarto.Preco_Diario}")
                case _:
                    print("Opção inválida para tipo de quarto.")

        case "2":
            print("\n--- Mostrar Informações ---")
            print("1 - Informações quarto luxo")
            print("2 - Informações quarto simples")
            print("3 - Informações hóspede")
            print("4 - Informações recepcionista")
            print("5 - Informações técnico de recepção")

            sub_op = input("Escolha uma opção: ")

            match sub_op:
                case "1":
                    if lista_quarto_luxo:
                        for q in lista_quarto_luxo:
                            q.mostrar_informacoes()
                    else:
                        print("Nenhum quarto de luxo cadastrado.")
                case "2":
                    if lista_quarto_simples:
                        for q in lista_quarto_simples:
                            q.mostrar_informacoes()
                    else:
                        print("Nenhum quarto simples cadastrado.")
                case "3":
                    if lista_hospede:
                        for h in lista_hospede:
                            h.mostrar_informacoes()
                    else:
                        print("Nenhum hóspede registrado.")
                case "4":
                    if lista_recepcionista:
                        for r in lista_recepcionista:
                            r.mostrar_informacoes()
                    else:
                        print("Nenhum recepcionista registrado.")
                case "5":
                    if lista_tecnico_recepcao:
                        for t in lista_tecnico_recepcao:
                            t.mostrar_informacoes()
                    else:
                        print("Nenhum técnico de recepção registrado.")
                case _:
                    print("Opção inválida.")

        case "3":
            print("1 - Quarto de luxo")
            print("2 - Quarto simples")
            op_q = input("Escolha uma opção: ")

            match op_q:
                case "1":
                    Preco_Diario = float(input("Insira o preço diário do quarto de luxo: "))
                    ID_Quarto_luxo += 1
                    q = quarto_luxo(ID_Quarto_luxo, Preco_Diario, ID_Quarto_luxo)
                    lista_quarto_luxo.append(q)
                    print("Quarto de luxo cadastrado com sucesso!")
                case "2":
                    Preco_Diario = float(input("Insira o preço diário do quarto simples: "))
                    ID_Quarto_simples += 1
                    Q = Quarto_simples(ID_Quarto_simples, Preco_Diario, ID_Quarto_simples)
                    lista_quarto_simples.append(Q)
                    print("Quarto simples cadastrado com sucesso!")
                case _:
                    print("Opção inválida.")

        case "4":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            salario = float(input("Salário: "))
            especialidade = input("Defina a sua especialidade: ")
            T = tecnico_manutencao(nome, idade, salario, especialidade)
            lista_especialidade.append(T)
            print("Técnico de manutenção registado com sucesso!")

        case "5":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            salario = float(input("Salário: "))
            turno = input("Turno (manha/tarde/noite): ").lower()
            id_func += 1
            R = recepcionista(nome, id_func, idade, salario, turno)
            lista_recepcionista.append(R)
            print("Recepcionista cadastrado com sucesso!")

        case "6":
            print("1 - Manhã")
            print("2 - Tarde")
            print("3 - Noite")
            turno_opcao = input("Opção: ")
            match turno_opcao:
                case "1":
                    print("Turno escolhido: Manhã")
                case "2":
                    print("Turno escolhido: Tarde")
                case "3":
                    print("Turno escolhido: Noite")
                case _:
                    print("Opção inválida.")

        case "7":
            if not lista_tecnico_recepcao:
                print("Nenhum técnico de recepção disponível!")
            else:
                descricao = input("Descreva o reparo: ")
                lista_tecnico_recepcao[0].registrar_reparo(descricao)

        case "0":
            print("Saindo do sistema...")
            break

        case _:
            print("Opção inválida. Tente novamente.")