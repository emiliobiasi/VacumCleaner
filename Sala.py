import random
import numpy

class Sala:
    def __init__(self, status, cleaner):
        # cria salas sujas
        if status > 0:
            self.sujo = 1
            self.cleaner_here = cleaner
            self.chao = [[random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
                         [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
                         [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]]
        # cria salas limpas
        else:
            self.sujo = 0
            self.cleaner_here = cleaner
            self.chao = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]

    def set_cleaner_here(self, cleaner):
        self.cleaner_here = cleaner

    def set_chao(self):
        index = random.randint(0, 2)
        index2 = random.randint(0, 2)
        self.chao[index][index2] = "X"


    def __str__(self):
        return "sujo? : " + self.sujo.__str__(), "cleaner? : " + self.cleaner_here.__str__(), "chao : " + self.chao.__str__()
