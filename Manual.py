# # Faz o Cleaner limpar a sala em que está
# def limpar(salas, cleaner):
#     salas[cleaner.sala].limpa()
#
#
# # Move o Cleaner para a sala da direita
# def mover_direita(salas, index):
#     salas[index].unset_cleaner_here()
#     if len(salas) != index:
#         salas[index + 1].set_cleaner_here()
#     else:
#         print("Não é possíver ir para direta! As salas ja acabaram para este lado.")
#
#
# # Move o Cleaner para a sala da esquerda
# def mover_esquerda(salas, index):
#     salas[index].unset_cleaner_here()
#     if len(salas) != 1:
#         salas[index + 1].set_cleaner_here()
#     else:
#         print("Não é possíver ir para esquerda! As salas ja acabaram para este lado.")
