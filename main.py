from Salas import Salas
from Sala import Sala

qtd_salas = int(input("Digite a quantidade de salas : "))
while not 0 < qtd_salas < 11:
    print("Digite no mínimo 1 sala e no máximo 10!")
    qtd_salas = int(input("Digite a quantidade de salas : "))
qtd_sujas = int(input("Quantas delas estão sujas? : "))

# Qual ambiente voce deseja? Base ou Onisciente

# Qual controlador deseja utilizar?
# Em caso de ambiente Base: opcoes -> controlador robo-base ou manual
# Em caso de ambiente Onisciente: opcoes -> controlador robo-Onisciente ou manual

minha_casa = Salas(qtd_salas, qtd_sujas)

for i in range(len(minha_casa.vetor_salas)):
    print(minha_casa.vetor_salas[i].__str__())

