# 1. Criar e coletar uma matriz [4][3] inteiro com quantidade de produtos vendidaos em 4 semanas. Calcule e exiba:
#   a) A quantidade de cada produto vendido no mês;
#   b) A quantidade de produtos vendidos por semana;
#   c) O total de produtos vendidos no mês.
# Produto: A  B  C
matriz = [[[],[],[]], # Semana 1
          [[],[],[]], # Semana 2
          [[],[],[]], # Semana 3
          [[],[],[]]] # Semana 4
# Ordem: | A | B | C |
vendasMensaisIndividuais = []
# Ordem: | Semana 1 | Semana 2 | Semana 3 | Semana 4 |
totalDeVendasSemanais = []
totalDeVendasMensais = 0


for coluna in range(3):
    if (coluna == 0):
        print("PRODUTO: A")
    elif (coluna == 1):
        print("PRODUTO: B")
    elif (coluna == 2):
        print("PRODUTO: C")
    elif (coluna == 3):
        print("PRODUTO: D")
    for linha in range(4):
        qtde = (int(input("Digite a quantidade de vendas desse produto na {}º semana: ".format((linha + 1)))))
        matriz[linha][coluna] = qtde
        # print(matriz)

for coluna in range(3):
    soma = 0
    for linha in range(4):
        soma += matriz[linha][coluna]
    vendasMensaisIndividuais.append(soma)
    # print(vendasMensaisIndividuais)

for linha in range(4):
    soma = 0
    for coluna in range(3):
        soma += matriz[linha][coluna]
    totalDeVendasSemanais.append(soma)
    print(totalDeVendasSemanais)

for valor in vendasMensaisIndividuais:
    totalDeVendasMensais += valor
    # print(totalDeVendasMensais)

print("TOTAL DE VENDAS MENSAIS:")
for i in range(len(vendasMensaisIndividuais)):
    if (i == 0):
        print("PRODUTO A: {}".format(vendasMensaisIndividuais[0]))
    if (i == 1):
        print("PRODUTO B: {}".format(vendasMensaisIndividuais[1]))
    if (i == 2):
        print("PRODUTO C: {}".format(vendasMensaisIndividuais[2]))

print("TOTAL DE VENDAS SEMANAIS:")
for i in range(len(totalDeVendasSemanais)):
    if (i == 0):
        print("SEMANA 1: {} VENDAS".format(totalDeVendasSemanais[0]))
    if (i == 1):
        print("SEMANA 2: {} VENDAS".format(totalDeVendasSemanais[1]))
    if (i == 2):
        print("SEMANA 3: {} VENDAS".format(totalDeVendasSemanais[2]))
    if (i == 3):
        print("SEMANA 4: {} VENDAS".format(totalDeVendasSemanais[3]))

print("TOTAL DE VENDAS NO MÊS: {}".format(totalDeVendasMensais))