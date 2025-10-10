# 21: Receba quatro notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média: 1.Se a média for >= 6.0, exiba: "APROVADO"; 2. Se a média for >= 3.0 e < 6.0, exiba "EXAME"; 3. Se a média for < 3.0, exiba "RETIDO".
media = (((float(input("Digite a primeira nota do aluno: "))) + (float(input("Digite a segunda nota do aluno: "))) + (float(input("Digite a terceira nota do aluno: "))) + (float(input("Digite a quarta nota do aluno: ")))) / 4)
if (media >= 6.0):
    print("A média final do aluno é igual a {}, portanto, ele ESTÁ APROVADO!!!".format(media))
elif (media >= 3.0):
    print("A média final do aluno é igual a {}, portanto, ele FARÁ O EXAME!!!".format(media))
else:
    print("A média final do aluno é igual a {}, portanto, ele ESTÁ RETIDO!!!".format(media))