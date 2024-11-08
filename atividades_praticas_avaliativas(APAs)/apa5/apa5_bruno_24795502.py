###################################################
# PUC - CAMPINAS
# Prof. Msc. Luã Marcelo Muriana
# Algoritmos de Programação, Projetos e Computação
# Engenharia de Software 2024/2
# Atividade Prática 5 - Torre de Panquecas
# Nome: Bruno César Goncalves Lima Mota 
# RA: 24795502
###################################################
torre = [int(panqueca)for panqueca in input().split()]
temporaria = [] #cria uma lista temporaria
while True:
  espatula = int(input()) 
  if espatula == 0: #se for 0 da break
    break
  temporaria = [] #reinicia a variavel temporaria apos o usuario digitar o movimento da espatula
  for i in range(espatula-1,-1,-1): #vai de onde a espatula esta ate o topo dela
    temporaria.append(torre[i]) #coloca o valor na nova lista 
  
  for i in range(espatula): #depois de adicionar na lista temporaria, coloco a ordem q ta na lista dentro das panquecas so q agora com elas viradas 
    torre[i] = temporaria[i]
for i in range(len(torre)-1): #se o primeiro numero da lista for maior que o segunda ent quer dizer q a torre ficou instavel
    if torre[i] > torre[i+1]:
        print('Torre instavel')
        break
else:
    print('Torre estavel')
            
        
        
        
        

        
    