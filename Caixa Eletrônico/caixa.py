# QTDE DE CÉDULAS:| 200 | 100 | 50 | 20 | 10 | 5 |
saldoCaixa = [                    # BANCO:
            [[],[],[],[],[],[],], # Banco do Brasil
            [[],[],[],[],[],[],], # Santander
            [[],[],[],[],[],[],], # Itaú
            [[],[],[],[],[],[],], # Caixa
]
def carregarNotas():
    global saldoCaixa
    # Carregar quantidade de cédulas de cada valor:
    for linha in range(4):
        for coluna in range(6):
            saldoCaixa[linha][coluna] = 1000
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
                retirarNotas(saldoCaixa)
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