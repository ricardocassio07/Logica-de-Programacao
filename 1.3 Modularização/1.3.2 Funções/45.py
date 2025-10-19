# 45: Caldule e mostre o resultado da série 1 - 2/4 + 3/9 - 4/16 + 5/25 + ... + 15/225.
resultado = 0
for i in range(1, (15 + 1)):
    if ((i % 2) == 0):
        resultado -= (i / (i * i))
    else:
        resultado += (i / (i * i))
print("O resultado da série é {}!".format(resultado))