# 5. Carregar código das peças em um tabuleiro de xadrez, onde:
# CÓDIGO|  1 |  2  |  3  |   4  |  5   | 6 |  7  |
# PEÇA  |PEÃO|TORRE|BISPO|CAVALO|RAINHA|REI|VAZIO|
#   Calcular e mostrar a soma das peças do tabuleiro.
#   -> NÃO PODE UTILIZAR ESTRUTURA DE DECISÃO E ESCOLHA CASO NA CONTAGEM DAS PEÇAS <-

tab = [
    [2,1,3,4,5,6,7,2],
    [1,1,1,1,1,1,1,1],
    [7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7],
    [1,1,1,1,1,1,1,1],
    [2,1,3,4,5,6,7,2],
]

codigos = [0, 0, 0, 0, 0, 0, 0]
soma = 0

for linha in range(8):
    for codigo in range(8):
        soma += tab[linha][codigo]
        codigos[((tab[linha][codigo]) - 1)] += 1

print("SOMA = {}".format(soma))
print("PEÃO = {}".format(codigos[0]))
print("TORRE = {}".format(codigos[1]))
print("BISPO = {}".format(codigos[2]))
print("CAVALO = {}".format(codigos[3]))
print("RAINHA = {}".format(codigos[4]))
print("REI = {}".format(codigos[5]))
print("VAZIO = {}".format(codigos[6]))
