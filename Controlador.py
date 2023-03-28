from Salas import Salas


# Controlador de ROBO manual do usuário
def manual_base(qtd_salas, qtd_sujas, cleaner):
    print("\n------ CONTROLADOR MANUAL - AMBIENTE BASE ------")
    salas = Salas(qtd_salas, qtd_sujas, cleaner)
    for i in range(len(salas.vetor_salas)):
        print(salas.vetor_salas[i].__str2__())

    print("\n------ OPCOES DO CONTROLE ------")
    print("1 - Limpar")
    print("2 - Andar para a direita")
    print("3 - Andar para a esquerda")

    # Criando um dicionário para simular o switch case
    options = {
        1: cleaner.limpar,
        2: cleaner.mover_direita,
        3: cleaner.mover_esquerda
    }

    # Definindo a escolha
    escolha = int(input("Opcao: "))

    # Executando a opção escolhida
    options[escolha](salas)
    for i in range(len(salas.vetor_salas)):
        print(salas.vetor_salas[i].__str2__())


def manual_onisciente(qtd_salas, qtd_sujas, cleaner):
    print("\n------ CONTROLADOR MANUAL - AMBIENTE ONISCIENTE ------")
    salas = Salas(qtd_salas, qtd_sujas, cleaner)
    for i in range(len(salas.vetor_salas)):
        print(salas.vetor_salas[i].__str__())

    print("\n------ OPCOES DO CONTROLE ------")
    print("1 - Limpar")
    print("2 - Andar para a direita")
    print("3 - Andar para a esquerda")

    # Criando um dicionário para simular o switch case
    options = {
        1: cleaner.limpar,
        2: cleaner.mover_direita,
        3: cleaner.mover_esquerda
    }

    # Definindo a escolha
    escolha = int(input("Opcao: "))

    # Executando a opção escolhida
    options[escolha](salas)

    for i in range(len(salas.vetor_salas)):
        print(salas.vetor_salas[i].__str__())


# Proximas lógicas
