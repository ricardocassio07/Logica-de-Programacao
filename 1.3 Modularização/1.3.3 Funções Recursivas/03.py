# Calcular a série: (1/1) + (1/2) + (1/3) + ... + (1/100):
def somar(n):
    if (n > 1):
        return 1/(n + somar(n - 1))
    else:
        return 1
print(somar(100))