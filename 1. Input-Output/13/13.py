# 13: Receba a quantidade de alimentos em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
qtdAlimentos = (float(input("Digite a quantidade total de alimentos em kilogramas (Kg): ")))
duracao = ((qtdAlimentos/(50/1000)))
print("Os {}Kg de alimentos será suficiente para alimentar essa pessoa por {} dias!!!".format(qtdAlimentos, duracao))