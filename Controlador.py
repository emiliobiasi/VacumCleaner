# Função que printa as salas
def printando_tabela_salas_onisciente(salas):
    print("\n------------ SALAS ------------")
    print_salas = "\n| SUJO? | "
    for i in range(len(salas.vetor_salas)):
        print_salas = print_salas + salas.vetor_salas[i].sujo.__str__() + " | "
    print(print_salas)

    print_robo = "\n| ROBO? | "
    for i in range(len(salas.vetor_salas)):
        print_robo = print_robo + salas.vetor_salas[i].cleaner_here.__str__() + " | "
    print(print_robo)


def printando_tabela_salas_base(salas, cleaner):
    print("\n------------ SALAS ------------")
    print_salas = "\n| SUJO? | "
    for i in range(len(salas.vetor_salas)):
        if i != cleaner.sala:
            print_salas = f"{print_salas} {salas.vetor_salas[i].visivel} | "
        else:
            print_salas = f"{print_salas} {salas.vetor_salas[i].sujo.__str__()} | "

    print(print_salas)

    print_robo = "\n| ROBO? | "
    for i in range(len(salas.vetor_salas)):
        print_robo = f"{print_robo} {salas.vetor_salas[i].cleaner_here.__str__()} | "
    print(print_robo)


# Controlador de ROBO robo-base
def logica_robo_base(salas, cleaner):
    while cleaner.sala != 0:
        if cleaner.verifica_limpo(salas) == 1:
            cleaner.limpar(salas)
            cleaner.atualiza_memoria()
        cleaner.mover_esquerda(salas)

    while cleaner.sala != len(salas.vetor_salas) - 1:
        if cleaner.verifica_limpo(salas) == 1:
            cleaner.limpar(salas)
            cleaner.atualiza_memoria()
        cleaner.mover_direita(salas)

    if cleaner.verifica_limpo(salas) == 1:
        cleaner.limpar(salas)
        cleaner.atualiza_memoria()


# Verifica a sujeira mais distante a esquerda e a direita do robo
def verifica_sujeira_longe(salas, cleaner):
    ret = [0, 0]

    posicao_robo = cleaner.sala
    while posicao_robo != -1:
        if salas.vetor_salas[posicao_robo].sujo == 1:
            ret[0] = posicao_robo
        posicao_robo -= 1

    posicao_robo = cleaner.sala
    while posicao_robo != len(salas.vetor_salas):
        if salas.vetor_salas[posicao_robo].sujo == 1:
            ret[1] = posicao_robo
        posicao_robo += 1
    return ret


def esquerda_primeiro(salas, cleaner, ret):
    while cleaner.sala != ret[0]:
        if cleaner.verifica_limpo(salas) == 1:
            cleaner.limpar(salas)
            cleaner.atualiza_memoria()
        cleaner.mover_esquerda(salas)

    while cleaner.sala != ret[1]:
        if cleaner.verifica_limpo(salas) == 1:
            cleaner.limpar(salas)
            cleaner.atualiza_memoria()
        cleaner.mover_direita(salas)

    if cleaner.verifica_limpo(salas) == 1:
        cleaner.limpar(salas)
        cleaner.atualiza_memoria()


def direita_primeiro(salas, cleaner, ret):
    while cleaner.sala != ret[1]:
        if cleaner.verifica_limpo(salas) == 1:
            cleaner.limpar(salas)
            cleaner.atualiza_memoria()
        cleaner.mover_direita(salas)

    while cleaner.sala != ret[0]:
        if cleaner.verifica_limpo(salas) == 1:
            cleaner.limpar(salas)
            cleaner.atualiza_memoria()
        cleaner.mover_esquerda(salas)

    if cleaner.verifica_limpo(salas) == 1:
        cleaner.limpar(salas)
        cleaner.atualiza_memoria()


def logica_robo_onisciente(salas, cleaner, ret):
    distancia_esquerda = cleaner.sala - ret[0]
    distancia_direita = ret[1] - cleaner.sala

    if distancia_esquerda <= distancia_direita:
        esquerda_primeiro(salas, cleaner, ret)
    else:
        direita_primeiro(salas, cleaner, ret)


def robo_base(salas, cleaner):
    print("\n------ CONTROLADOR BASE - AMBIENTE BASE ------")
    printando_tabela_salas_base(salas, cleaner)

    print("\n\nROBO LIMPANDO...")

    # Algorítimo que faz o robo limpar todas as salas de forma autônoma BASE
    logica_robo_base(salas, cleaner)

    # -------------------------------------------------------------------

    print("\n\nResultado: ")
    print(f"\nO Robo limpou as {len(cleaner.memoria)} salas que estavam sujas.")
    print(f"Salas que estavam sujas: {cleaner.memoria}\n")
    printando_tabela_salas_onisciente(salas)


# Controlador de ROBO base manual do usuário
def manual_base(salas, cleaner):
    print("\n------ CONTROLADOR MANUAL - AMBIENTE BASE ------")
    printando_tabela_salas_base(salas, cleaner)

    escolha = 1
    while escolha != 0:
        print("\n------ OPCOES DO CONTROLE ------")
        print("1 - Limpar")
        print("2 - Andar para a direita")
        print("3 - Andar para a esquerda")
        print("0 - Parar programa")

        # Criando um dicionário para simular o switch case
        options = {
            1: cleaner.limpar,
            2: cleaner.mover_direita,
            3: cleaner.mover_esquerda
        }

        # Definindo a escolha
        escolha = int(input("\nOpcao: "))

        # Executando a opção escolhida
        options[escolha](salas)
        printando_tabela_salas_base(salas, cleaner)


# Controlador de ROBO robo-onisciente
def robo_onisciente(salas, cleaner):
    print("\n------ CONTROLADOR ONISCIENTE - AMBIENTE ONISCIENTE ------")
    printando_tabela_salas_onisciente(salas)

    print("\n\nROBO LIMPANDO...")

    # Algorítimo que faz o robo limpar todas as salas de forma autônoma ONISCIENTE com base nas sujeiras mais
    # distantes do robo
    logica_robo_onisciente(salas, cleaner, verifica_sujeira_longe(salas, cleaner))

    # -------------------------------------------------------------------

    print("\n\nResultado: ")
    print(f"\nO Robo limpou as {len(cleaner.memoria)} salas que estavam sujas.")
    print(f"Salas que estavam sujas: {cleaner.memoria}\n")
    printando_tabela_salas_onisciente(salas)


# Controlador de ROBO Onisciente manual do usuário
def manual_onisciente(salas, cleaner):
    print("\n------ CONTROLADOR MANUAL - AMBIENTE ONISCIENTE ------")
    printando_tabela_salas_onisciente(salas)

    escolha = 1
    while escolha != 0:
        print("\n------ OPCOES DO CONTROLE ------")
        print("1 - Limpar")
        print("2 - Andar para a direita")
        print("3 - Andar para a esquerda")
        print("0 - Parar programa")

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

        printando_tabela_salas_onisciente(salas)
