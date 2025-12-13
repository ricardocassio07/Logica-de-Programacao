# 8. Crie uma função recursiva que exiba o resultado do fatorial de um número (Pela limitação da recursividade, o número de entrada deverá ser baixo para não dar estouro(limite de entrada = 12)): 
def fatorial(n):
    if n > 12:
        return "ENTRADA MUITO ALTA!"
    if n < 0:
        return "NÚMERO INVÁLIDO!"
    if n >= 1:
        return n * fatorial(n - 1)
    else:
        return 1
print(fatorial(1))