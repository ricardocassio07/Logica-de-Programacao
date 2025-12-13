# 9. Crie uma função recursiva que exiba o total de elementos negatvos de um vetor de inteiros, de N posições, passado como parâmetro: 
def qtdeNegativos(vetor, n):
    if (n - 1) == 0:
        return 0
    if vetor[n - 1] < 0:
        return 0 + qtdeNegativos(lista, n - 1)
    else:
        return 1 + qtdeNegativos(lista, n - 1)
lista = [-1, -3, 5, -90, 100, 89, 3, -2]
print(qtdeNegativos(lista, len(lista)))