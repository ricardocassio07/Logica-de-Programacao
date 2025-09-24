# 30: Receba a data de nascimento e a data atual em ano, mês e dia. Calcule e mostre a idade em anos, mese e dias, considerando os anos bissextos:

# Looping para verificar a coerência das informações:
verificado = False
while (verificado == False):
    # Inserção de dados:
    diaN = (int(input("Digite o dia de nascimento: ")))
    mesN = (int(input("Digite o mês de nascimento: ")))
    anoN = (int(input("Digite o ano de nascimento: ")))

    diaA = (int(input("Digite o dia atual: ")))
    mesA = (int(input("Digite o mês atual: ")))
    anoA = (int(input("Digite o ano atual: ")))
    dataDeNascimento = ("válida")
    if ((diaN <= 30) and (mesN == 4 or mesN == 6 or mesN == 9 or mesN == 11)):
        dataDeNascimento = ("válida")
    elif (diaN <= 31) and (mesN == 1 or mesN == 3 or mesN == 5 or mesN == 7 or mesN == 8 or mesN == 10 or mesN == 12):
        dataDeNascimento = ("válida")
    elif ((diaN <= 29) and (mesN == 2)and ((anoN % 400 == 0) or (anoN % 4 == 0 and anoN % 100 != 0))):
        dataDeNascimento = ("válida")
    elif ((diaN <= 28) and (mesN == 2) and ((anoN % 400 != 0) or (anoN % 4 == 0 and anoN % 100 != 0))):
        dataDeNascimento = ("válida")
    else:
        dataDeNascimento = ("inválida")

    dataAtual = ("válida")
    if ((diaA <= 30) and (mesA == 4 or mesA == 6 or mesA == 9 or mesA == 11)):
        dataAtual = ("válida")
    elif (diaA <= 31) and (mesA == 1 or mesA == 3 or mesA == 5 or mesA == 7 or mesA == 8 or mesA == 10 or mesA == 12):
        dataAtual = ("válida")
    elif ((diaA <= 29) and (mesA == 2)and ((anoA % 400 == 0) or (anoA % 4 == 0 and anoA % 100 != 0))):
        dataAtual = ("válida")
    elif ((diaA <= 28) and (mesA == 2) and ((anoA % 400 != 0) or (anoA % 4 == 0 and anoA % 100 != 0))):
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

# Se os dados forem coerentes...:
if (verificado == True):
    # Calcula a diferença de anos:
    diferencaA = (anoA - anoN)

    if (mesA < mesN):
        # Se o mês atual for menor que o de nascimento, significa que a pessoa ainda não fez aniversário...
        # Então, temos que subtrair um ano da diferença, pois ele não se passou completamente:
        diferencaA -= 1
        # Nós vamos retirar aquele ano retirado para realizar o cálculo da diferença dos meses, para isso, vamos converte-lô para 12 meses
        # Depois disso, devemos retirar o valor do mês atual e acrescentar o valor do mês de nascimento.
        # Dessa forma, nós vamos conseguir calcular quantos meses se passaram desde o último aniversário.
        diferencaM = ((12 - mesA) + mesN)
    else:
        # Se o mesA for maior ou igual ao mesN, basta nós subtrairmos para descobrir a difereça.
        diferencaM = (mesA - mesN)

    if (diaA < diaN):
        # Se o dia atual for menor que o dia de nascimento, significa que a pessoa ainda não completou mais um mês de vida, logo, precisamos contar os dias desde o mesmo dia no mês anterior até o dia atual..
        # Então, devemos retirar um mês da diferença de meses:
        diferencaM -= 1
        # Para saber quantos dias faltam pro próximo mês, olhamos pro mês antes do atual (mês do último "mesversário"...):
        mesAnterior = (mesA - 1)
        # E depois, devemos considerar a quantidade de dias que aquele mês tem, subtrair o dia de nascimento, para descobriirmos quantos dias após o "mesversário", e acrescentar o dia atual:
        if (mesAnterior == 4 or mesAnterior == 6 or mesAnterior == 9 or mesAnterior == 11):
            diferencaD = ((30 - diaN) + diaA)
        elif (mesAnterior == 2):
            if ((anoA % 400 == 0) or (anoA % 4 == 0 and anoA % 100 != 0)):
                diferencaD = ((29 - diaN) + diaA)
            else:
                diferencaD = ((28 - diaN) + diaA)
        else:
            diferencaD = ((31 - diaN) + diaA)
    else:
        # Se o diaA for maior ou igual ao diaN, basta nós encontramos a diferença entre eles:
        diferencaD = (diaA - diaN)

    print("Entre {}/{}/{} e {}/{}/{} se passaram {} dia(s), {} mês(es) e {} ano(s)!".format(diaN, mesN, anoN, diaA, mesA, anoA, diferencaD, diferencaM, diferencaA))