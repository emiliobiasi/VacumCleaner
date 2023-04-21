import random

from Cleaner import Cleaner
from Sala import Sala


class Salas:

    def __init__(self, qtd_salas, qnt_sujas, cleaner):
        self.vetor_salas = []
        self.qnt_sujas = qnt_sujas

        # Cria a quantidade de salas desejadas
        for i in range(qtd_salas):
            s = Sala(qnt_sujas, "_")
            self.vetor_salas.append(s)
            qnt_sujas = qnt_sujas - 1

        # Embaralhar as salas dentro do vetor após criação
        random.shuffle(self.vetor_salas)

        # Coloca o Cleaner em uma sala aleatoria
        self.vetor_salas[cleaner.sala].set_cleaner_here(cleaner)

    def __str__(self):
        return self.vetor_salas.__str__()

    def verifica_sujeira(self):
        for i in range(len(self.vetor_salas)):
            if self.vetor_salas[i].sujo == 1:
                return True
        return False