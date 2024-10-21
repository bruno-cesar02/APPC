###################################################
# PUC - CAMPINAS
# Prof. Msc. Luã Marcelo Muriana
# Algoritmos de Programação, Projetos e Computação
# Engenharia de Software 2024/2
# Atividade Prática 2 - Ingresso de Cinema
# Nome: Bruno César Gonçalves Lima Mota
# RA: 24795502
###################################################
DiaDaSemana = int(input())
Hora_InicioSessão = float(input())
Minuto_InícioSessão = float(input())
Estudante = str(input())
Metodo_pagamento = str(input())

#ver se é de vespertino ou notuno 
if Hora_InicioSessão < 18 or (Hora_InicioSessão == 18 and Minuto_InícioSessão <30):
    periodo = 'vespertino'
else:
    periodo ='noturno'

#preço base conforme dia da semana e o periodo
if DiaDaSemana == 1: #domingo
    preco_base = 30.00

elif DiaDaSemana == 2: #segunda
   if periodo == "vespertino":
      preco_base = 15.00
   else: 
       preco_base = 20.00

elif DiaDaSemana == 3: #terca
    if periodo == "vespertino":
      preco_base = 15.00
    else: 
       preco_base = 20.00

elif DiaDaSemana == 4: #quarta
    if periodo == "vespertino":
      preco_base = 15.00
    else: 
       preco_base = 30.00

elif DiaDaSemana == 5: #quinta
    if periodo == "vespertino":
      preco_base = 20.00
    else: 
       preco_base = 30.00

elif DiaDaSemana == 6: #sexta
    if periodo == "vespertino":
      preco_base = 20.00
    else: 
       preco_base = 40.00

elif DiaDaSemana == 7: #sabado
    if periodo == "vespertino":
      preco_base = 30.00
    else: 
       preco_base = 40.00

#ver se é estudande
if Estudante =='S' :
   ingresso = preco_base / 2 # o estudante vai pagar meia entrada ou seja 50% de desconto
else:
   #aplicar desconto com o cartao
   if Metodo_pagamento =='C':
        if DiaDaSemana == 1: #domingo
          desconto = 0.30
        elif DiaDaSemana == 2 or DiaDaSemana == 3 or DiaDaSemana == 4 or DiaDaSemana == 5: #segunda a quinta
          desconto = 0.50
        elif DiaDaSemana == 6: #sexta
            if periodo =='vespertino':
              desconto = 0.50
            else:
              desconto = 0.30    
        elif DiaDaSemana ==7: #sabado
           desconto = 0.20
        ingresso = preco_base *(1 - desconto) #aplicando o desconto
   else:
      ingresso = preco_base #sem desconto pra pagamento em dinheiro fisico

      # Exibir o valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))
