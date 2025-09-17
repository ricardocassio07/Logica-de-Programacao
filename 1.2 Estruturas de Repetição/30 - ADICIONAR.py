# 30: Receba a data de nascimento e a data atual em ano, mês e dia. Calcule e mostre a idade em anos, mese e dias, considerando os anos bissextos:
diaN = (int(input("Digite o dia de nascimento: ")))
mesN = (int(input("Digite o mês de nascimento: ")))
anoN = (int(input("Digite o ano de nascimento: ")))

diaA = (int(input("Digite o dia atual: ")))
mesA = (int(input("Digite o mês atual: ")))
anoA = (int(input("Digite o ano atual: ")))

verificado = False
while (verificado == False):
    dataDeNascimento = ("válida")
    if ((diaN <= 30) and (mesN == 4 or mesN == 6 or mesN == 9 or mesN == 11)):
        dataDeNascimento = ("válida")
    elif (diaN <= 31) and (mesN == 1 or mesN == 3 or mesN == 5 or mesN == 7 or mesN == 8 or mesN == 10 or mesN == 12):
        dataDeNascimento = ("válida")
    elif ((diaN <= 29) and (mesN == 2)and (anoN % 4 == 0)):
        dataDeNascimento = ("válida")
    elif ((diaN <= 28) and (mesN == 2) and (anoN % 4 != 0)):
        dataDeNascimento = ("válida")
    else:
        dataDeNascimento = ("inválida")

    dataAtual = ("válida")
    if ((diaA <= 30) and (mesA == 4 or mesA == 6 or mesA == 9 or mesA == 11)):
        dataAtual = ("válida")
    elif (diaA <= 31) and (mesA == 1 or mesA == 3 or mesA == 5 or mesA == 7 or mesA == 8 or mesA == 10 or mesA == 12):
        dataAtual = ("válida")
    elif ((diaA <= 29) and (mesA == 2)and (anoA % 4 == 0)):
        dataAtual = ("válida")
    elif ((diaA <= 28) and (mesA == 2) and (anoA % 4 != 0)):
        dataAtual = ("válida")
    else:
        dataAtual = ("inválida")

    if (dataDeNascimento == ("válida") and dataAtual == ("válida") and (anoN <= anoA)):
        verificado = True
    elif (dataAtual == "inválida"):
        print("A data {}/{}/{} NÃO É VÁLIDA!!!".format(diaA, mesA, anoA))
    elif (dataDeNascimento == "inválida"):
        print("A data {}/{}/{} NÃO É VÁLIDA!!!".format(diaN, mesN, anoN))
    elif (anoN > anoA):
        print("Ano de nascimento inválido!!! O ano de nascimento não pode ser maior que o atual!!!")
    
if (verificado == True):
    diferencaA = (anoA - anoN)

    for i in range(anoN, (anoA + 1), 1):
        if (i % 4 == 0):
            diferencaD += 1
        if (diferencaD == 30):
            diferencaM += 1
            diferencaD = 0

    if (mesA < mesN):
        diferencaA -= 1
        diferencaM = ((12 - mesA) + mesN)
    else:
        diferencaM = (mesA - mesN)

    if (diaA < diaN):
        diferencaM -= 1
        diferencaD = ((30 - diaN) + diaA)
    else:
        diferencaD = (diaA - diaN)