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


def menu_aleatorio():
    print('\n------ ESCOLHA DE ALEATORIEDADE ------')
    controlador = 0
    while controlador not in ['1', '2']:
        print('1 - Sem aleatoriedade')
        print('2 - Com aleatoriedade')
        controlador = input('\nQual opção você deseja? ')
    return controlador
