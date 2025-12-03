#  5. Criar e coletar em um vetor [20] inteiro. Calcule e exiba, segundo: ¹⁰∑i=₁(A[1] - A[21 - 1])
vetor = []
for i in range(20):
    num = (int(input("{}- Digite um número: ".format((i + 1)))))
    vetor.append(num)
soma = 0
for i in range(10):
    soma += (vetor[i] - vetor[(19 - i)])
print(soma)