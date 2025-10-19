# 43: Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria, sabendo que Ana tem 1,10m e cresce 3cm ao ano e Maria tem 1,50m e cresce 2cm ao ano.
alturaAna = 1.10
alturaMaria = 1.50
tempo = 0
while (alturaAna <= alturaMaria):
    alturaAna += 0.03
    alturaMaria += 0.02
    tempo += 1
print("Serão necessários {} anos para que Ana seja maior que Maria!".format(tempo))