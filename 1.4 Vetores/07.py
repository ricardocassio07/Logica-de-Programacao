# 7. A partir do exercício 6 (vetor ordenado) solicitar um valor qualquer e veirifcar a sua existência no vetor (utilizar pesquisa binária)
vetor = []
for i in range(20):
    num = (int(input("Digite um número: ")))
    vetor.append(num)
comprimento = len(vetor)
for i in range((comprimento - 1)):
    for j in range((comprimento - 1 - i)):
        if (vetor[j] > vetor[(j + 1)]):
            temp = vetor[j]
            vetor[j] = vetor[(j + 1)]
            vetor[(j + 1)] = temp
numDesejado = (int(input("Digite um número qualquer: ")))
print(vetor)
inicio = 0
fim = (len(vetor) - 1)
encontrado = False
while (encontrado == False):
    meio = ((inicio + fim) // 2)
    if (vetor[meio] == numDesejado):
        encontrado = True
    elif (numDesejado > vetor[meio]):
        inicio = (meio + 1)
    else:
        fim = (meio - 1)
if (encontrado == True):
    print("está")
else:
    print("ñ está")

