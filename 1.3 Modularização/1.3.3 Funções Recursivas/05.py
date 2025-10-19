# Calcular a série: (n)! + (n - 1)! + (n - 2)! + ... + (1)!
def somar(n):
    if ((n == 1) or (n == 0)):
        return 1
    else:
        return fatorial(n) + somar(n - 1)
def fatorial(n):
    if (n == 1):
        return 1
    else:
        return n * fatorial (n - 1)
print(somar(3))