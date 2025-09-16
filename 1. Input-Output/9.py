# 9: Receba 2 números inteiros. Calcule o quadrado de cada um, some-os e mostre o resultado.
x = (int(input("Digite um número: ")))
y = (int(input("Digite outro número: ")))
resultado = ((x ** 2) + (y ** 2))
print("{}² + {}² = {:.2f}".format(x, y, resultado))