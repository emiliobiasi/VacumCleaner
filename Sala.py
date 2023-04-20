from Cleaner import Cleaner


class Sala:
    def __init__(self, status, cleaner):
        # cria salas sujas
        if status > 0:
            self.sujo = 1
            self.visivel = "?"
            self.cleaner_here = cleaner

        # cria salas limpas
        else:
            self.sujo = 0
            self.visivel = "?"
            self.cleaner_here = cleaner

    def sujar_sala(self):
        self.sujo = 1

    def set_cleaner_here(self, cleaner):
        self.cleaner_here = cleaner

    def unset_cleaner_here(self):
        self.cleaner_here = "_"

    def limpa(self):
        self.sujo = 0

    def __str__(self):
        return "sujo? : " + self.sujo.__str__(), "cleaner? : " + self.cleaner_here.__str__()

    def __str2__(self):
        return "sujo? : " + self.visivel.__str__(), "cleaner? : " + self.cleaner_here.__str__()


