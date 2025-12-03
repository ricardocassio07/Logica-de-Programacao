# 1. Criar e coletr um vetor [50] inteiro. Calcular e exibir:
#   a) A média dos valores entre 10 e 200;
#   b) A soma dos números ímpares.
def calcularMedia(vetor):
    soma = 0
    qtdeNum = 0
    for i in range(len(vetor)):
        if (10 < vetor[i] < 200):
            soma += vetor[i]
            qtdeNum += 1
    return (soma/qtdeNum)
def calcularSoma(vetor):
    soma = 0
    for i in range(len(vetor)):
        if (vetor[i] % 2 != 0):
            soma += vetor[i]
    return soma
vetor = []
for i in range(50):
    num = (int(input("{}- DIGITE UM NÚMERO: ".format((i + 1)))))
    vetor.append(num)
media = calcularMedia(vetor)
soma = calcularSoma(vetor)
print("A média dos valores que estão entre 10 e 200 é {}!".format(media))
print("A soma dos valores ímpares é {}!".format(soma))
