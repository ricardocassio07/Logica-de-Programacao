# 38. Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.
i = 0
menor = 0
maior = 0
while (i < 10):
    n = (float(input("Digite um número real e positivo: ")))
    if (n > 0):
        if ((menor == 0) and (maior == 0)):
            menor = n
            maior = n
        if (n > maior):
            maior = n
        if (n < menor):
            menor = n
    else:
        print("O número deve ser real e positivo!")
    i += 1
print("O menor número digitado foi {}!".format(menor))
print("O maior número digitado foi {}!".format(maior))