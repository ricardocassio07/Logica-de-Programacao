'''
    28: Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
    Venda Mensal | Preço Atual | Preço Novo
        <500           <30          +10%
    >=500 e <1000  >=30 e < 80      +15%
       >=1000         >=80          -5%
    Obs.: Para outras condições, preço novo será igual ao preço atual.
'''
preco = (float(input("Digite o preço atual do produto: R$")))
mediaVendas = (float(input("Digite a média mensal de vendas desse produto: ")))
if ((mediaVendas>=1000)and(preco>=80)):
    preco *= 0.95
elif ((mediaVendas>=500)and(preco>=30)):
    preco *= 1.15
elif((mediaVendas<500)and(preco<30)):
    preco *= 1.10
else:
    preco = preco
print("O novo preço do produto é R${:.2f}".format(preco))