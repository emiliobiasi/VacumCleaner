class Cleaner:
    def __init__(self, index_sala):
        self.sala = index_sala
        self.memoria = []

    # Faz o Cleaner limpar a sala em que está
    def limpar(self, salas):
        salas.vetor_salas[self.sala].limpa()

    # Move o Cleaner para a sala da direita
    def mover_direita(self, salas):
        if int(len(salas.vetor_salas)) != (self.sala + 1) and len(salas.vetor_salas) != 1:
            salas.vetor_salas[self.sala].unset_cleaner_here()
            salas.vetor_salas[self.sala + 1].set_cleaner_here(self)
            self.sala = self.sala + 1
        else:
            print("Não é possíver ir para direta! As salas ja acabaram para este lado.")

    # Move o Cleaner para a sala da esquerda
    def mover_esquerda(self, salas):
        if self.sala > 0:
            salas.vetor_salas[self.sala].unset_cleaner_here()
            salas.vetor_salas[self.sala - 1].set_cleaner_here(self)
            self.sala = self.sala - 1
        else:
            print("Não é possíver ir para esquerda! As salas ja acabaram para este lado.")

    # Verifica se esta limpo ou sujo o quarto em que o robo está
    def verifica_limpo(self, salas):
        return salas.vetor_salas[self.sala].sujo

    # Marca na memoria do robo os lugares que limpou
    def atualiza_memoria(self):
        self.memoria.append(self.sala + 1)

    def __str__(self):
        return "▲"
