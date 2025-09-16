# 5: Receba os coeficientes A, B e C de uma equação do 2º grau (Ax² + Bx + C = 0). Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes).
print("Sabendo que a estrutura da equação do segundo grau é: Ax² + Bx + C = 0")
A = (float(input("Digite o coeficiente 'A' da equação: ")))
B = (float(input("Digite o coeficiente 'B' da equação: ")))
C = (float(input("Digite o coeficiente 'C' da equação: ")))
delta = (((B**2) - (4*A*C)))
if (delta >= 0):
    x1 = (((-1*B) - (delta**0.5)) / (2*A))
    x2 = (((-1*B) + (delta**0.5)) / (2*A))
    print("x1 = {:.2f} e x2 = {:.2f}".format(x1, x2))
else:
    print("A equação não possui raízes reais!!!")