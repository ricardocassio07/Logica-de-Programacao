# Receba um número. Calcule e mostre os resultados da tabuada desse número.
n = (int(input("Digite um número inteiro: ")))
for i in range(11):
    resultado = (n * i)
    print("{} x {} = {}".format(n, i, resultado))