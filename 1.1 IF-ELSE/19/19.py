# 19: Receba 2 valores reais. Calcule e mostre o maior deles.
x = (float(input("Digite um número real: ")))
y = (float(input("Digite outro número real: ")))
if (x > y):
    print("Entre {} e {}, o maior número é {}!".format(x, y, x))
else:
    print("Entre {} e {}, o maior número é {}!".format(x, y, y))