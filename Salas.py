import random

from Sala import Sala


class Salas:

    def __init__(self, qtd_salas, qnt_sujas):
        self.vetor_salas = []
        self.qnt_sujas = qnt_sujas

        # Cria a quantidade de salas desejadas
        for i in range(qtd_salas):
            s = Sala(qnt_sujas, 0)
            self.vetor_salas.append(s)
            qnt_sujas = qnt_sujas - 1

        # Coloca o Cleaner em uma sala aleatoria
        index = random.randint(0, len(self.vetor_salas) - 1)
        self.vetor_salas[index].set_cleaner_here(1)

        # Embaralhar as salas dentro do vetor após criação
        random.shuffle(self.vetor_salas)

    def __str__(self):
        return self.vetor_salas.__str__()
