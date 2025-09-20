# 20: Receba 3 coeficientes A, B e C de uma equação do 2º grau (Ax² + Bx + C = 0). Verifique e mostre a existência de raízes reais e se caso exista, calcule-as e mostre-as.
print("Sabendo que Ax² + Bx + C = 0")
A = (float(input("Digite um valor para o coeficiente 'A': ")))
B = (float(input("Digite um valor para o coeficiente 'B': ")))
C = (float(input("Digite um valor para o coeficiente 'C': ")))
delta = ((B**2) - (4*A*C))
if (delta >= 0):
    x1 = (((-1*B) - (delta**0.5))/(2*A))
    x2 = (((-1*B) + (delta**0.5))/(2*A))
    print("As raízes para a equação são {} e {}.".format(x1, x2))
else:
    print("Não existem raízes reais para a equação!!!")