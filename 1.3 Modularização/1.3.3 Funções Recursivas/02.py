# Calcular a série: (n) + (n-1) + (n-2) + ... + (n-n), utilizando funções recursivas.
def serie(n):
    if (n > 0):
        return n + serie(n - 1)
    else:
        return 0
num = (int(input("Digite um número inteiro: ")))
print(serie(num))