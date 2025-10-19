# 36. Receba um número N. Calcule e mostre a série 1 + (1/2!) + ... + (1/N!).
n = (int(input("Digite um número inteiro: ")))
fatorial = 1
resultado = 1
for i in range(1, (n + 1)):
    fatorial *= i
    resultado += (1/fatorial)
print("O resultado é {}".format(resultado))