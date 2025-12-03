# 4.Criar e coletar em um vetor [30] real e calcular e exibir:
#   a) A média do grupo;
#   b) A quatidade de notas acima da média do grupo;
#   c) As posições dos valores abaixo da média do grupo.
def calcularMedia(vetor):
    soma = 0
    qtdeNum = 0
    for num in vetor:
        soma += num
        qtdeNum += 1
    return (soma/qtdeNum)
vetor = []
for i in range (5):
    num = (int(input("Digite a nota do {}º aluno: ".format((i + 1)))))
    vetor.append(num)
media = calcularMedia(vetor)
qtdeNotasAcimaDaMedia = 0
posicoesNotasMenores = []
for num in vetor:
    if (num > media):
        qtdeNotasAcimaDaMedia += 1
    if (num < media):
        posicoesNotasMenores.append(vetor.index(num))
print("A média dos alunos é {}!".format(media))
print("A quantidade de notas acima da média é {}!".format(qtdeNotasAcimaDaMedia))
print("A(s) posição(ções) da(s) nota(s) abaixo da média no vetor é {}!".format(posicoesNotasMenores))