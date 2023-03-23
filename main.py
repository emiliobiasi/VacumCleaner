from Salas import Salas
from Sala import Sala

qtd_salas = int(input("Digite a quantidade de salas: "))
qtd_sujas = int(input("Quantas delas estão sujas? : "))

minha_casa = Salas(qtd_salas, qtd_sujas)

for i in range(len(minha_casa.vetor_salas)):
    print(minha_casa.vetor_salas[i].__str__())

