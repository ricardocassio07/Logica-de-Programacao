# 14: Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.
anguloUm = (float(input("Digite o valor de um dos ãngulos do triângulo: ")))
anguloDois = (float(input("Digite o valor do segundo ângulo desse triângulo: ")))
anguloTres = (180 - anguloUm - anguloDois)
print("O valor do terceiro ângulo do triângulo, cujos seus outros ângulos medem {}u.n. e {}u.n., é {}u.n.".format(anguloUm, anguloDois, anguloTres))