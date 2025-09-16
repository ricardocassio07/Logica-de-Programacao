# 6: Receba os valores em "x" e "y". Efetue a troca de seus valores e mostre os seus conteúdos.
x = (float(input("Digite um valor para x: ")))
y = (float(input("Digite um valor para y: ")))
parametro:float
parametro = y
y = x
x = parametro
print("x = {}\ny = {}".format(x, y))