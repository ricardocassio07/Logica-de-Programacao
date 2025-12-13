# 17: Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12Km/L. Receba o tempo do percuso e a velocidade média.
qtdCombustivel = ((float(input("Digite o tempo do percuso, em horas: ")) * float(input("Digite a velocidade média da viagem, em Km/h: "))) / 12)
print("Foram gastos {} litros de combustível!!!".format(qtdCombustivel))