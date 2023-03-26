import random
import numpy

class Sala:
    def __init__(self, status, cleaner):
        # cria salas sujas
        if status > 0:
            self.sujo = 1
            self.cleaner_here = cleaner

        # cria salas limpas
        else:
            self.sujo = 0
            self.cleaner_here = cleaner


    def set_cleaner_here(self, cleaner):
        self.cleaner_here = cleaner


    def __str__(self):
        return "sujo? : " + self.sujo.__str__(), "cleaner? : " + self.cleaner_here.__str__()
