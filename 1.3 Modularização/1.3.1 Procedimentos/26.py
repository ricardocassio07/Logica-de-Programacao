# 26: Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.
A = (int(input("Digite um número inteiro: ")))
B = (int(input("Digite outro número inteiro: ")))
if (A%B == 0):
    print("O número {} é múltiplo do número {}!!!".format(A, B))
else:
    print("O número {} não é múltiplo do número {}!!!".format(A, B))