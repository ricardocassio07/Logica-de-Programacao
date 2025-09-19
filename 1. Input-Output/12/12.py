# 12: Receba o ano de nascimento de uma pessoa e o ano atual. Calcule e mostre sua idade e quantos anos ela terá daqui a 17 anos.
anoNas = (int(input("Digite o ano em que a pessoa nasceu: ")))
anoAtual = (int(input("Digite o ano atual: ")))
idade = (anoAtual - anoNas)
idadeFutura = (idade + 17)
print("Essa pessoa tem {} anos de idade e daqui a 17 anos, ela terá {} anos de idade!!!".format(idade, idadeFutura))