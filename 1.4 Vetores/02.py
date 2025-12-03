# 2. Criar e coletar um vetor [100] inteiro e exibir:
#   a) O menor e maior valor;
#   b) A média dos valores.
def maior_e_menor(vetor):
    maior = 0
    menor = 0
    for num in vetor:
        if (vetor.index(num) == 0):
            maior = menor = num
        if (num > maior):
            maior = num
        if (num < menor):
            menor = num
    print("Maior número: {}".format(maior))
    print("Menor número: {}".format(menor))
def media(vetor):
    soma = 0
    qtdeNum = 0
    for num in vetor:
        soma += num
        qtdeNum += 1
    return (soma/qtdeNum)
vetor = []
for i in range(100):
    num = (int(input("{}- DIGITE UM NÚMERO: ".format((i + 1)))))
    vetor.append(num)
maior_e_menor(vetor)
print("A média dos valores inseridos é {}!".format(media(vetor)))