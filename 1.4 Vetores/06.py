# 6. Criar e coletar um vetor [20] com números aleatórios. Classificar este vetor em ordem crescente e mostre os dados.
# -> BUBBLE SORT <-
vetor = []
for i in range(5):
    num = (int(input("Digite um número: ")))
    vetor.append(num)
comprimento = len(vetor)
for i in range((comprimento - 1)):
    for j in range((comprimento - 1 - i)):
        if (vetor[j] > vetor[(j + 1)]):
            temp = vetor[j]
            vetor[j] = vetor[(j + 1)]
            vetor[(j + 1)] = temp
print(vetor)
