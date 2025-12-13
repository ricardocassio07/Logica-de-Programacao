# 7. Criar uma função recursiva que, recebendo um vetor de inteiros, o tamanho do vetor e o valor da última posição do vetor como o primeiro menor valor, retorne o menor valor contido neste vetor. 
def acharValor(vetor, tamanho, ultimoValor):
    menorValor = ultimoValor
    if vetor[tamanho - 1] < menorValor:
        menorValor = vetor[tamanho - 1]
    if tamanho > 1:
        return acharValor(vetor, (tamanho - 1), menorValor)
    else:
        return menorValor
vetor = [1, 2, 3, 4, 5]
print(acharValor(vetor, 5, 5))