valorDesejado = (int(input()))
print()

valor = [0] * 5
DM = (valorDesejado - (valorDesejado % 10000))
print(DM)
UM = (valorDesejado - DM)
C = UM
UM = (UM - (UM % 1000))
print(UM)
C = C % 1000
D = (C % 100)
C = C - D
U = D % 10
D = D - U
print(C)
print(D)
print(U)
valor[0] = DM
valor[1] = UM
valor[2] = C
valor[3] = D
valor[4] = U
print(valor)
DezenaMilhar = (valor[0] / 100)
print(DezenaMilhar)

print()
UnidadeMilhar = valor[1] / 100
print(UnidadeMilhar)

print()
Centena = valor[2] / 100
print(Centena)

print()
Dezena = valor[3] / 10
print(Dezena)


# Final '2' significa nota de 2 reais, final '5' siginifca nota de cinco, 
Unidade = valor[4]
if (Unidade == 1):
    print("-> NÃO É POSSÍVEL SACAR ESSE VALOR <-")
elif (Unidade == 2):
    Unidade = 12 # 1: Uma nota 2: R$2,00 -> 12
elif (Unidade == 3):
    print("-> NÃO É POSSÍVEL SACAR ESSE VALOR <-")
elif (Unidade == 4):
    Unidade = 22 # 1: Duas notas 2: R$2,00 -> 12
elif (Unidade == 5):
    Unidade = 15 # 1: Uma nota 5: R$5,00 -> 15
elif (Unidade == 6):
    Unidade = 32 # 3: Três notas 2: R$2,00 -> 32
elif (Unidade == 7): 
    Unidade = 1215 # 1: Uma nota 2: R$2,00 1: Uma nota 5: R$5,00 -> 1215
elif (Unidade == 8):
    Unidade = 42 # 4: Quatro notas 2: R$2,00 -> 42
elif (Unidade == 9):
    Unidade = 2215 # 2: Duas notas 2: R$2,00 1: Uma nota 5: R$5,00

notas = []                                                                                            # QUANTIDADE DE NOTAS:
notas.append([[DezenaMilhar], [UnidadeMilhar], [Centena], [Dezena], [Unidade]])                       # | x * 100| x * 100 | x * 100 | x * 10 | x * NOTAS DE 2 OU DE 5 |
if (valor[3] % 20 == 0):
    notas.append([[DezenaMilhar * 2], [UnidadeMilhar * 2], [Centena * 2], [Dezena / 2], [Unidade]]) # | x * 50 | x * 50  | x * 50  | x * 20  | x * NOTAS DE 2 OU DE 5 |
elif (valor[3] % 5 == 0):
    notas.append([[DezenaMilhar * 2], [UnidadeMilhar * 2], [Centena * 2], [Dezena * 2], [Unidade]]) # | x * 50 | x * 50  | x * 50  | x * 5  | x * NOTAS DE 2 OU DE 5 |
if (valor[3] % 20 == 0):
    notas.append([[DezenaMilhar * 5], [UnidadeMilhar * 5], [Centena * 5], [Dezena / 2], [Unidade]]) # | x * 20 | x * 20  | x * 20  | x * 20  | x * NOTAS DE 2 OU DE 5 |
elif (valor[3] % 5 == 0):
    notas.append([[DezenaMilhar * 5], [UnidadeMilhar * 5], [Centena * 5], [Dezena * 2], [Unidade]]) # | x * 20 | x * 20  | x * 20  | x * 5  | x * NOTAS DE 2 OU DE 5 |
print(notas)
