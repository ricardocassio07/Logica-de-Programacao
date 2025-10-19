# 42: Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99.
x = 0
soma = 0
for i in range(1, (50 + 1)):
    x = ((2 * i) - 1)
    soma += (i / x)
print("O resultado da série é {}!".format(soma))