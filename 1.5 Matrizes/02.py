# 2. Criar e carregar uma matriz [4][4] com números aleatórios, sendo que a diagonal principal terá seus dados carregados no programa a seguir:
#   |1 |  |  |  |
#   |  |4 |  |  |
#   |  |  |16|  |
#   |  |  |  |64|
matriz = [
    [[],[],[],[]],
    [[],[],[],[]],
    [[],[],[],[]],
    [[],[],[],[]]
]
base = 4
expoente = 0
for linha in range(4):
    for coluna in range(4):
        if (linha == coluna):
            matriz[linha][coluna] = (base ** expoente)
            expoente += 1
        else:
            num = (int(input("L:[{}]C:[{}] - DIGITE UM NÚMERO: ".format((linha + 1), (coluna + 1)))))
            matriz[linha][coluna] = num
# print(matriz)
dados = []
for linha in matriz:
    print(linha)