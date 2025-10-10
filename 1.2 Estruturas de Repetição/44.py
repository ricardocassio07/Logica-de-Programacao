# 44: Receba o número da base e do expoente. Calcule e mostrw o valor da potência.
base = (float(input("Digite o valor da base:\n-> ")))
expoente = (float(input("Digite o valor do expoente:\n-> ")))
resultado = base
i = 1
if ((expoente == 0) & (base != 0)):
    resultado = 1
elif ((base == 0) & (expoente == 0)):
    resultado = "INDERTEMINADO"
else:
    while (i < expoente):
        resultado *= base
        i += 1
print("{}^{} = {}".format(base, expoente, resultado))