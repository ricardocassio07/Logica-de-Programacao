# 40. Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.
n1 = (int(input("Digite um número inteiro: ")))
n2 = (int(input("Digite outro número inteiro: ")))
if (n1 > n2):
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
print("Entre o número {} e {} estão os seguintes números primos: ".format(menor, maior))
while (menor < (maior - 1)):
    menor += 1
    qtde_de_divisores = 0
    for i in range(2, menor):
        if (menor % i == 0):
            qtde_de_divisores += 1
    if (qtde_de_divisores == 0):
        print(menor)
    qtde_de_divisores = 0