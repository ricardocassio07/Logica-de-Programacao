continuar = True
while (continuar == True):
    try:
        opc = (int(input("O QUE DESEJA:\nDIGITE:\n1- Carregar Notas\n2- Retirar Notas\n3- Estatística\n9- Encerrar\n-> ")))
        if ((1 <= opc <= 3) or (opc == 9)):

        else:
            print("-> OPÇÃO INVÁLIDA <-")
    except ValueError:
        print("-> OPÇÃO INVÁLIDA <-")