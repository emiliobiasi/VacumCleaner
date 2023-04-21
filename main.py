import random
from Cleaner import Cleaner
from Controlador import manual_base, manual_onisciente, robo_base, robo_onisciente
from ControladorAleatorio import robo_onisciente_aleatorio
from Salas import Salas
from menufile import menu_controlador, menu_ambiente, menu_aleatorio

qtd_salas = 0
while not 0 < qtd_salas < 11:
    qtd_salas = int(input("Digite a quantidade de salas (1 a 10): "))
qtd_sujas = int(input("Quantas delas estão sujas? : "))

# Criando cleaner e as salas
index = random.randint(0, qtd_salas - 1)
cleaner = Cleaner(index)
salas = Salas(qtd_salas, qtd_sujas, cleaner)
# Define se o ambiente terá aleatoriedade ou não
aux = menu_aleatorio()
if aux == '2':
    robo_onisciente_aleatorio(salas, cleaner)
else:
    # --------------------------------------------------------

    # Qual controlador deseja utilizar?----
    # Em caso de ambiente Base: opcoes -> controlador robo-base ou manual
    # Em caso de ambiente Onisciente: opcoes -> controlador robo-Onisciente ou manual

    # ------------------------- EXEC -------------------------

    menuresult = menu_controlador(menu_ambiente())
    print(f"\nVocê digitou: {menuresult}")

    if menuresult[0] == "1" and menuresult[1] == "1":
        robo_base(salas, cleaner)

    elif menuresult[0] == "1" and menuresult[1] == "2":
        manual_base(salas, cleaner)

    elif menuresult[0] == "2" and menuresult[1] == "1":
        robo_onisciente(salas, cleaner)

    elif menuresult[0] == "2" and menuresult[1] == "2":
        manual_onisciente(salas, cleaner)
