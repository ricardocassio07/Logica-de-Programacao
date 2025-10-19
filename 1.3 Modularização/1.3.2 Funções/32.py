# 32: Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N
n = (int(input("Digite um número: ")))
resultado = 0
for i in range(1, n + 1):
    resultado += (1/i)
print(resultado)