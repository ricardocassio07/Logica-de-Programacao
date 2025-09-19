# 16: Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que será as horas horas trabalhadas multiplicadas pelo valor da hora. Calcule o salário o líquido (= Salário Bruto - Desconto). A cada dependente será acrescido R$ 100,00 no Salário Líquido. Exiba o salário a receber.
qtdHoras = (float(input("Digite a quantidade de horas trabalhadas: ")))
valorHora = (float(input("Digite o valor da hora: ")))
salarioBruto = (qtdHoras * valorHora)
percentualDesconto = (float(input("Digite o percentual de desconto em decimal: ")))
nDependentes = (float(input("Digite o número de dependentes: ")))
salarioLiquido = ((salarioBruto - (percentualDesconto * salarioBruto)) + (100 * nDependentes))
print("O trabalhador irá receber R$ {:.2f}".format(salarioLiquido))