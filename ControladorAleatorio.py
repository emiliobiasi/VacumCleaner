from Controlador import verifica_sujeira_longe, printando_tabela_salas_onisciente
import random


def implanta_sujeira_aleatoriamente(salas):
    aux = random.randint(0, 9)
    if aux >= 7:
        sala_suja = random.randint(0, len(salas.vetor_salas) - 1)
        salas.vetor_salas[sala_suja].sujar_sala()


def robo_onisciente_aleatorio(salas, cleaner):
    printando_tabela_salas_onisciente(salas)
    while salas.verifica_sujeira():
        implanta_sujeira_aleatoriamente(salas)
        logica_robo_onisciente_aleatorio(salas, cleaner, verifica_sujeira_longe_aleatorio(salas, cleaner))
        printando_tabela_salas_onisciente(salas)
    printando_tabela_salas_onisciente(salas)


# Verifica a sujeira mais distante a esquerda e a direita do robo
def verifica_sujeira_longe_aleatorio(salas, cleaner):
    ret = [None, None]

    posicao_robo = cleaner.sala - 1
    while posicao_robo != -1:
        if salas.vetor_salas[posicao_robo].sujo == 1:
            ret[0] = posicao_robo
        posicao_robo -= 1

    posicao_robo = cleaner.sala + 1
    while posicao_robo != len(salas.vetor_salas):
        if salas.vetor_salas[posicao_robo].sujo == 1:
            ret[1] = posicao_robo
        posicao_robo += 1

    if ret[0] is not None:
        # distancia-esquerda
        ret[0] = cleaner.sala - ret[0]

    if ret[1] is not None:
        # distancia_direita
        ret[1] = ret[1] - cleaner.sala

    return ret


def logica_robo_onisciente_aleatorio(salas, cleaner, vet):
    if cleaner.verifica_limpo(salas) == 1:
        cleaner.limpar(salas)
        cleaner.atualiza_memoria()

    if vet[1] is None:
        cleaner.mover_esquerda(salas)
    elif vet[0] is None:
        cleaner.mover_direita(salas)
    elif vet[0] <= vet[1]:
        cleaner.mover_esquerda(salas)
    else:
        cleaner.mover_direita(salas)

