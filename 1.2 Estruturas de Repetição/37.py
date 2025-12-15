# 37. Receba um número inteiro. Calcule e mostre a série Fibonacci até o N'nésimo termo.
n = (int(input("Digite um número inteiro: ")))
x = 0
y = 1
for i in range(1, (n + 1)):
    temp = x
    x += y
    y = temp
print("O {}º elemento da série é {}!".format(n, x))
    
