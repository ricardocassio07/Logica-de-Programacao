# 35. Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre eles.
x = (int(input("Digite um número inteiro: ")))
y = (int(input("Digite outro número inteiro: ")))
if (x>y):
    maior = x
    menor = y
else:
    maior = y
    menor = x
menor += 1
while (menor<maior):
    if (menor % 2 != 0):
        print(menor)
    menor += 1