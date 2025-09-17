# 39. Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
'''
    Casa: 1, 2, 3, 4, ..., 64
    Qtde: 1, 2, 4, 8, ..., N
'''
i = 0
total = 0
while (i < 64):
    qtde = (2 ** i)
    total += qtde
    i += 1
print("A soma da quantidade de grãos contidos no tabuleiro é igual a {} !".format(total))