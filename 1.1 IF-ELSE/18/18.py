# 18: Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor.
x = (int(input("Digite um número inteiro: ")))
y = (int(input("Digite outro número inteiro: ")))
diferenca:int
if (x > y):
    diferenca = (x - y)
else:
    diferenca = (y - x)
print("A diferença entre {} e {} é igual a {}".format(x, y, diferenca))
