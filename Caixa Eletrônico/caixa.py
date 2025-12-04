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
                valor = 25
            elif (coluna == 3):
                valor = 10
            elif (coluna == 4):
                valor = 5
            elif (coluna == 5):
                valor = 2
            while True:
                try:
                    qtde = (int(input("DIGITE A QUANTIDADE DE NOTAS DE R${}: ".format(valor))))
                    if (qtde <= 100):
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
                valor = (str(valorDesejado))

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