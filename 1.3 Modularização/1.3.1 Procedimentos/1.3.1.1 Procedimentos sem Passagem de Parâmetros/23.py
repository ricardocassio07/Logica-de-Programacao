# 23: Receba 3 valores obrigatoria em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 em ordem.
print("Digite 3 números em ordem crescente e um 4º não necessariamente em ordem!!!")
A = (float(input("Digite um número: ")))
B = (float(input("Digite mais um número: ")))
C = (float(input("Digite mais um número: ")))
D = (float(input("Digite o último número: ")))
if ((A < B) and (B < C)):
    if (D < A):
        print(f"{D} - {A} - {B} - {C}")
    elif (D < B):
        print(f"{A} - {D} - {B} - {C}")
    elif (D < C):
        print(f"{A} - {B} - {D} - {C}")
    else:
        print(f"{A} - {B} - {C} - {D}")
else:
    print("Você digitou os números de maneira incorreta!!!")