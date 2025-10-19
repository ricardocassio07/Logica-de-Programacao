# Calcular a série: 1 + 2 + 3 + ... + 100, utilizando funções recursivas
def calcular(n):
    if (n == 0):
        return 0
    return n + calcular(n - 1)
resultado = calcular(100)
print(resultado)