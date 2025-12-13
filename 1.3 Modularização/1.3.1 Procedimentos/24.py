# 24: Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3:
n = (int(input("Digite um número inteiro: ")))
if((n%2 == 0) and (n%3 == 0)):
    print("O número {} é divisível por 2 e 3!!!".format(n))
else:
    print("O número {} não é divisível por 2 e 3!!!".format(n))