# 3. Criar e coletar valores inteiros nos vetores 21[3] e vt2[3]. Concatenar esses valores em um 3º vetor (vt3[6]) e mostrar os seus resultados. (vt1|1|2|3| vt2|4|5|6| vt3|1|2|3|4|5|6|)
vt1 = []
print("VT1:")
for i in range(3):
    num = (int(input("{} - Digite um número: ".format((i + 1)))))
    vt1.append(num)
vt2 = []
print("VT2:")
for i in range(3):
    num = (int(input("{} - Digite um número: ".format((i + 1)))))
    vt2.append(num)
vt3 = []
for i in range(6):
    if (0 <= i <= 2):
        vt3.append(vt1[i])
    if (i > 2):
        vt3.append(vt2[(i - 3)])
print(vt3)
