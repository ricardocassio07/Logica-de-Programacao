# Calcule a série:  (n / 1) + (n - 1/2) (n - 2/3) + ... + (1 / n)
def fracao(numerador, denominador):
    divisao = (numerador/denominador)
    if (numerador == 1):
        return divisao
    else:
        return divisao + fracao((numerador - 1), (denominador + 1))

num = (int(input("Digite um número inteiro: ")))
print(fracao(num, 1))