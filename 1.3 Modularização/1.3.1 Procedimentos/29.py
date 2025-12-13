# 29: Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias, sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não são considerados.
tipo = (int(input("Digite o tipo de investimento: 1- Poupança 2- Renda Fixa\n-> ")))
valorDoInvestimento = (int(input("Digite o valor do investimento: R$")))
while ((tipo != 1) and (tipo != 2)):
    print("Tipo de investimento INVÁLIDO!!!!")
    tipo = (int(input("Digite o tipo de investimento: 1- Poupança 2- Renda Fixa\n-> ")))
if (tipo == 1):
    valorFinal = valorDoInvestimento * 1.03
else:
    valorFinal = valorDoInvestimento * 1.05
print("O valor inicial de invstimento (R${:.2f}), após 30 dias de aplicação, se tornaram R${:.2f}".format(valorDoInvestimento, valorFinal))