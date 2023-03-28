import random

from Cleaner import Cleaner
from Controlador import manual_base, manual_onisciente
from menufile import menu_controlador, menu_ambiente

qtd_salas = 0
while not 0 < qtd_salas < 11:
    qtd_salas = int(input("Digite a quantidade de salas (1 a 10): "))
qtd_sujas = int(input("Quantas delas estão sujas? : "))

index = random.randint(0, qtd_salas - 1)
cleaner = Cleaner(index)
# --------------------------------------------------------

# Qual controlador deseja utilizar?
# Em caso de ambiente Base: opcoes -> controlador robo-base ou manual
# Em caso de ambiente Onisciente: opcoes -> controlador robo-Onisciente ou manual

# ------------------------- EXEC -------------------------
menuresult = menu_controlador(menu_ambiente())
print(f"\nVocê digitou: {menuresult}")

if menuresult[0] == "1" and menuresult[1] == "1":
    print("\n------ AMBIENTE BASE e CONTROLADOR BASE ------")

elif menuresult[0] == "1" and menuresult[1] == "2":
    manual_base(qtd_salas, qtd_sujas, cleaner)

elif menuresult[0] == "2" and menuresult[1] == "1":
    print("\n------ AMBIENTE ONISCIENTE e CONTROLADOR ONISCIENTE ------")

elif menuresult[0] == "2" and menuresult[1] == "2":
    manual_onisciente(qtd_salas, qtd_sujas, cleaner)

