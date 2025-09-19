# 6: Receba os valores em "x" e "y". Efetue a troca de seus valores e mostre os seus conteúdos.
x = (input("Digite um valor para x: "))
y = (input("Digite um valor para y: "))
parametro:str
parametro = y
y = x
x = parametro
print("x = {}\ny = {}".format(x, y))