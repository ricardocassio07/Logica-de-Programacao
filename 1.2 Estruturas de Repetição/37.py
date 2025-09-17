# 37. Receba um número inteiro. Calcule e mostre a série Fibonacci até o N'nésimo termo.
n = (int(input("Digite um número inteiro: ")))
x = 0
y = 1
for i in range(1, (n + 1)):
    resultado = (x + y)
    print("O {}º termo da série é {}".format(i, resultado))
    if (i % 2 == 0):
        x = resultado
    else:
        y = resultado
