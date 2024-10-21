''' 3. Faça um programa que pergunte o preço de três produtos e informe qual produto você
deve comprar, sabendo que a decisão é sempre pelo mais barato'''
produto1 = float(input("Digite o preço do produto: "))
produto2 = float(input("Digite o preço do produto: "))
produto3 = float(input("Digite o preço do produto: "))
maisbarato = produto1
if produto1 >= 0 and produto2 >= 0 and produto3 >= 0:
    if produto2 <= maisbarato:
       maisbarato =produto2
    if produto3 <= maisbarato:
      maisbarato = produto3
    print(f'Compre o produto com o preço de {maisbarato:.2f} R$')
else:
    print("Sem preço")

