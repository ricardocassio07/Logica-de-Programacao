# 22: Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
x = (int(input("Digite um número inteiro: ")))
y = (int(input("Digite outro número inteiro: ")))
if (x > y):
    print(f"{y} - {x}")
else:
    print(f"{x} - {y}")