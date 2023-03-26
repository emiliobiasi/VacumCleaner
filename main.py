from Salas import Salas
from Sala import Sala

qtd_salas = 0
while not 0 < qtd_salas < 11:
    qtd_salas = int(input("Digite a quantidade de salas (1 a 10): "))
qtd_sujas = int(input("Quantas delas estão sujas? : "))


def menu_ambiente():
    ambiente = 0
    while ambiente not in ["1", "2"]:
        print("\n------ ESCOLHA DE AMBIENTE ------")
        print("1 - Ambiente Base")
        print("2 - Ambiente Onisciente")
        ambiente = input("Qual ambiente voce deseja? ")
    return ambiente


def menu_controlador(ambiente):
    print("\n------ ESCOLHA DE CONTROLADOR ------")
    if ambiente == "1":
        controlador = 0
        while controlador not in ["1", "2"]:
            print("1 - Controlador Robo-Base")
            print("2 - Controlador Manual")
            controlador = input("Qual controlador voce deseja? ")
        return ambiente, controlador
    else:
        controlador = 0
        while controlador not in ["1", "2"]:
            print("1 - Controlador Robo-Onisciente")
            print("2 - Controlador Manual")
            controlador = input("\nQual controlador voce deseja? ")
        return ambiente, controlador


# Qual controlador deseja utilizar?
# Em caso de ambiente Base: opcoes -> controlador robo-base ou manual
# Em caso de ambiente Onisciente: opcoes -> controlador robo-Onisciente ou manual

# ------------------------- EXEC -------------------------
menuresult = menu_controlador(menu_ambiente())
print(f"\nVocê digitou: {menuresult}\n")

if menuresult[0] == "1" and menuresult[1] == "1":
    print("\n------ AMBIENTE BASE e CONTROLADOR BASE ------")

elif menuresult[0] == "1" and menuresult[1] == "2":
    print("\n------ AMBIENTE BASE e CONTROLADOR MANUAL ------")
    salas = Salas(qtd_salas, qtd_sujas)
    for i in range(len(salas.vetor_salas)):
        print(salas.vetor_salas[i].__str2__())

elif menuresult[0] == "2" and menuresult[1] == "1":
    print("\n------ AMBIENTE ONISCIENTE e CONTROLADOR ONISCIENTE ------")

elif menuresult[0] == "2" and menuresult[1] == "2":
    print("\n------ AMBIENTE ONISCIENTE e CONTROLADOR MANUAL ------")
    salas = Salas(qtd_salas, qtd_sujas)
    for i in range(len(salas.vetor_salas)):
        print(salas.vetor_salas[i].__str__())





