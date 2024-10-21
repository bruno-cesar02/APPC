###################################################
# PUC - CAMPINAS
# Prof. Msc. Luã Marcelo Muriana
# Algoritmos de Programação, Projetos e Computação
# Engenharia de Software 2024/2
# Atividade Prática 3 - Controle de Estoque 
# Nome: Bruno César Gonçalves Lima Mota 
# RA: 24795502
###################################################

estoque = 0
vendas_realizadas = 0

pedido = int(input()) #vai ler o que o usuario digitou
while pedido != 0:
      
      if pedido > 0: #se for positivo vai adiciona o valor do pedido no estoque
          estoque = estoque + pedido
      elif pedido < 0:
          numero_venda = -pedido  #se for negativo é venda,entao transformo o numero negativo em positivo para colocar na parte da venda
          
          if numero_venda <= estoque: #se houver estoque o suficiente a venda é feita
              estoque -= numero_venda
              vendas_realizadas += 1
          elif numero_venda >= estoque:
              numero_venda = numero_venda * 1
              print(f'Quantidade indisponivel para a venda de {numero_venda} unidades.')
      pedido = int(input())
    
print(f'Quantidade de vendas realizadas: {vendas_realizadas}')
print(f'Quantidade em estoque: {estoque}')