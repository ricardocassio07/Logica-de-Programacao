# QTDE DE CÉDULAS:| 100 | 50 | 20 | 10 | 5 | 2 |
saldoCaixa = [                   # BANCO:
            [[],[],[],[],[],[]], # Banco do Brasil
            [[],[],[],[],[],[]], # Santander
            [[],[],[],[],[],[]], # Itaú
            [[],[],[],[],[],[]], # Caixa
]
def carregarNotas():
    global saldoCaixa
    # Carregar quantidade de cédulas de cada valor:
    for linha in range(4):
        if (linha == 0):
            print("BANCO DO BRASIL")
        elif (linha == 1):
            print("SANTANDER")
        elif (linha == 2):
            print("ITAÚ")
        elif (linha == 3):
            print("CAIXA")
        for coluna in range(6):
            if (coluna == 0):
                valor = 100
            elif (coluna == 1):
                valor = 50
            elif (coluna == 2):
                valor = 20
            elif (coluna == 3):
                valor = 10
            elif (coluna == 4):
                valor = 5
            elif (coluna == 5):
                valor = 2
            while True:
                try:
                    qtde = (int(input("DIGITE A QUANTIDADE DE NOTAS DE R${}: ".format(valor))))
                    if (qtde <= 250):
                        saldoCaixa[linha][coluna] = qtde
                    break
                except ValueError:
                    print("-> VALOR INVÁLIDO <-")

def retirarNotas():
    global saldoCaixa
    while True:
        try:
            digitoBanco = (int(input("DIGITE O CÓDIGO DO SEU BANCO:\nDIGITE:\n1- BANCO DO BRASIL\n2- SANTANDER\n3- ITAÚ\n4- CAIXA\n-> ")))
            if (1 <= digitoBanco <= 4):
                break
            else:
                print("-> OPÇÃO INVÁLIDA <-")
        except ValueError:
            print("-> VALOR INVÁLIDO <-")
    qtdeCelulasBancoDesejado = saldoCaixa[digitoBanco]
    valorDisponível = 0
    for coluna in saldoCaixa[digitoBanco]:
        valorDisponível += coluna
    # Lista que vai armazenar a quantidade de Dezenas de Milhar, Milhar, Centena, Dezena e Unidade:
    digitosDoValorDesejado = []
    while True:
        try:
            valorDesejado = (int(input("DIGITE O VALOR QUE DESEJA SACAR\n-> ")))
            if (valorDesejado > valorDisponível):
                print("-> SALDO DO CAIXA INSULFICIENTE <-")
            elif (valorDesejado < valorDisponível):
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

                numOpcoes = 0
                notas = []                                                                                            # QUANTIDADE DE NOTAS:
                notas.append([[DezenaMilhar + 10000], [UnidadeMilhar + 10000], [Centena + 10000], [Dezena], [Unidade]])                       # | x * 100| x * 100 | x * 100 | x * 10 | x * NOTAS DE 2 OU DE 5 |
                numOpcoes += 1
                if (valor[3] % 20 == 0):
                    notas.append([[(DezenaMilhar * 2) + 5000], [(UnidadeMilhar * 2) + 5000], [(Centena * 2) + 5000], [(Dezena / 2) + 2000], [Unidade]]) # | x * 50 | x * 50  | x * 50  | x * 20  | x * NOTAS DE 2 OU DE 5 |
                    numOpcoes += 1
                elif (valor[3] % 5 == 0):
                    notas.append([[DezenaMilhar * 2], [UnidadeMilhar * 2], [Centena * 2], [(Dezena * 2) + ], [Unidade]]) # | x * 50 | x * 50  | x * 50  | x * 5  | x * NOTAS DE 2 OU DE 5 |
                    numOpcoes += 1
                if (valor[3] % 20 == 0):
                    notas.append([[DezenaMilhar * 5], [UnidadeMilhar * 5], [Centena * 5], [Dezena / 2], [Unidade]]) # | x * 20 | x * 20  | x * 20  | x * 20  | x * NOTAS DE 2 OU DE 5 |
                    numOpcoes += 1
                elif (valor[3] % 5 == 0):
                    notas.append([[DezenaMilhar * 5], [UnidadeMilhar * 5], [Centena * 5], [Dezena * 2], [Unidade]]) # | x * 20 | x * 20  | x * 20  | x * 5  | x * NOTAS DE 2 OU DE 5 |
                    numOpcoes += 1
                numOpcoes = 0
                for opcao in notas:
                    numOpcoes += 1
                    valores = []
                    notasDeCem
                    notasDeCinquenta
                    notasDeVinte
                    notasDeDez
                    notasDeCinco
                    notasDeDois
                    if ()
                    print("{}.\n{} x R$100,00\n{} x R$50,00\n{} x R$20,00\n{} x R$10,00\n{} x R$5,00\n{} x R$2,00")

                while True:
                    try:
                        opc = 
                    except ValueError:
                        print("-> VALOR INVÁLIDO <-")
                
                print("-> QUANTIDADE DE CÉDULAS DE R${} INSULFICIENTES <-".format())
                print("-> POR FAVOR, SELECIONE UM VALOR SUPERIOR OU INFERIOR <-")
            else:
                break
        except ValueError:
            print("-> VALOR INVÁLIDO <-")

    
    

    
qtdeTotalCelulas = 0
numeroDeSaques = 0
continuar = True
while (continuar == True):
    try:
        opc = (int(input("O QUE DESEJA:\nDIGITE:\n1- Carregar Notas\n2- Retirar Notas\n3- Estatística\n9- Encerrar\n-> ")))
        if ((1 <= opc <= 3) or (opc == 9)):
            if (opc == 1):
                carregarNotas()
            elif (opc == 2):
                retirarNotas()
                numeroDeSaques += 1
            elif (opc == 3):
                estatisticas()
            elif (opc == 9):
                print("-> SESSÃO ENCERRADA <-")
                continuar = False
        else:
            print("-> OPÇÃO INVÁLIDA <-")
        for linha in range(4):
            for qtdeCelulas in range(6):
                qtdeTotalCelulas += qtdeCelulas
        if ((numeroDeSaques == 100) or (qtdeTotalCelulas == 0)):
            print("-> CAIXA ENCERRADO <-")
    except ValueError:
        print("-> OPÇÃO INVÁLIDA <-")