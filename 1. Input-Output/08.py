# 8: Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a.m.
valor = (float(input("Digite o valor do depósito: ")))
valorFinal = (valor * ((1 + 0.013) * 1))
print("O valor inicial de R${:.2f}, após 1 mês, se tornou R${:.2f}".format(valor, valorFinal))