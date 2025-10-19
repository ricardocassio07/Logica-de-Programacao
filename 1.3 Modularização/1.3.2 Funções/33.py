# 33: Receba um número inteiro. Calcule e mostre o seu fatorial.
n = (int(input("Digite um número inteiro: ")))
numDigitado = n
i = (n - 1)
while (i > 0):
    n *= i
    i -= 1
print("{}! = {}".format(numDigitado, n))