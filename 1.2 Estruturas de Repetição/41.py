# 41: Mostre todas as possibilidades de 2 dados caírem de forma que a soma tenha como resultado 7.
d1 = 1
d2 = 6
while (((d1 + d2) == 7) and ((d1 > 0) and (d2 > 0))):
    print("No primeiro dado pode cair o número {0} e no segundo dado pode cair o número {1}!".format(d1, d2))
    d1 += 1
    d2 -= 1
