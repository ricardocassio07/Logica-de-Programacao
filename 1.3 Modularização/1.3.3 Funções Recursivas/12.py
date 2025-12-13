# 12. Fazer, uma aplicação que resolva a soma de dois números naturais, sem a utilização de uma operação de soma (seja uma função aritmética ou oriunda que qualquer classe ou biblioteca), mas utilizando, apenas uma função recursiva de soma de 2 números.  
def somar(x, y):
    if y == 0:
        return x
    return somar((x + 1), (y - 1))
print(somar(5, 3))