# 10. Criar uma aplicação que tenha uma função recursiva que, recebendo um número inteiro (N), apresente a saída da somatória:
#   S = 1 + (1/2) + (1/3) + (1/4) + ... + (1/N)
def soma(n, i):
    if i == n:
        return 1/n
    return 1/i + soma(n, (i + 1))
print(soma(1, 1))