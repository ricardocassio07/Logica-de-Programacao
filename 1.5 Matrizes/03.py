# 3. Criar uma matriz [8][8] onde o programa irá carregar segundo:
# CASA |1|2|3|4|...|*EXIBA A SOMA DOS VALORES
# VALOR|1|2|4|8|...|
matriz = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]
base = 2
expoente = 0
soma = 0
for linha in range(8):
    for coluna in range(8):
        matriz[linha][coluna] = (base ** expoente)
        expoente += 1
        soma += matriz[linha][coluna]
print(soma)