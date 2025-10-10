# 27: Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em Km/h.
nVoltas = (int(input("Digite o número de voltas no circuito: ")))
extensao = (int(input("Digite a extensão do circuito em metros: ")))
tempo = (int(input("Digite o tempo de duração total da prova em minutos: ")))
# Convertendo o comprimento de pista de metros para kilometros:
extensao /= 1000
# Convertendo o tempo de prova de minutos para horas:
tempo /= 60
VM = ((nVoltas * extensao) / tempo)
print("A velocidade média é {} Km/h".format(VM))