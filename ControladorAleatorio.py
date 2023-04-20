from Controlador import verifica_sujeira_longe, logica_robo_onisciente
from Cleaner import Cleaner
from Salas import Salas
import random


def implanta_sujeira_aleatoriamente(salas):
    aux = random.randint(0, 9)
    print(aux)
    if aux >= 7:
        sala_suja = random.randint(1, len(salas.vetor_salas) - 1)
        salas.vetor_salas[sala_suja].sujar_sala()
        print(salas.vetor_salas[sala_suja].sujo)


def robo_onisciente_aleatorio(salas, cleaner):
    while salas.verifica_sujeira():
        implanta_sujeira_aleatoriamente(salas)
        logica_robo_onisciente_aleatorio(salas, cleaner, verifica_sujeira_longe(salas, cleaner))

def logica_robo_onisciente_aleatorio(salas,cleaner, vet):
    if cleaner.sala - vet[0] <= vet[1] - cleaner.sala:
        #logica mover esquerda aleatorio
    else:
        #logica mover direita aleatorio


qtd_salas = random.randint(1, 10)
cleaner = Cleaner(qtd_salas - 1)
salas = Salas(qtd_salas, random.randint(0, qtd_salas), cleaner)
robo_onisciente_aleatorio(salas, cleaner)
