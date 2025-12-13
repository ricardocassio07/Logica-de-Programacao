# 6. Criar uma aplicação em Java que tenha uma função recursiva que calcule o somatório do N primeiros número NATURAIS (a função deve retornar zero para números negativos) 
def soma(n):
    if n <= 0:
        return 0
    if n > 10:
        return "ENTRADA INVÁLIDA!"
    return n + soma(n-1)
print(soma(5))