# 4: Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura em graus Celsius. Calcule e mostre-a convertida em Fahrenheit (F) = ((9 * C + 160)/5)
temperaturaC = (float(input("Digite a temperatura em graus Celsius: ")))
temperaturaF = ((9 * temperaturaC + 160) / 5)
print("{}° Celsius é igual a {:.2f}° Fahrenheit".format(temperaturaC, temperaturaF))