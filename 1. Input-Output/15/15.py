# 15: Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre o valor da hipotenusa.
catetoUm = (float(input("Digite o valor de um dos catetos do triângulo: ")))
catetoDois = (float(input("Digite o valor do outro cateto do triângulo: ")))
hipotenusa = (((catetoUm ** 2) + (catetoDois ** 2)) ** 0.5)
print("O valor da hipotenusa do triângulo retângulo, cujo os seus catetos medem {} u.n. e {} u.n., é igual a {} u.n.".format(catetoUm, catetoDois, hipotenusa))
