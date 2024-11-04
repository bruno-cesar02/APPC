'''
lista = []
segmento = int(input('Digite a qtde de segmentos'))
soma = 0
import random
for i in range(20):
    numero_aleatorio = random.randint(-100, 100)
    lista.append(numero_aleatorio)
for i in range (segmento):
    x = lista.pop()
    if x >=0:
        soma+=x
    elif x <= 0:
        soma -= x 
print(soma)
'''
soma2 = 0
soma1 = 0
lista = [5,2,-2,-7,3,14,10,-3,9]
segmento = int(input("digite o segmento : "))
for i in range(len(lista)):
    for j in range (segmento):
        limite = (i - len(lista)) - segmento
          
          if soma1 >= soma2:
              soma2 = soma1
          else: soma2 = soma2 
print(soma1)
print(soma2)