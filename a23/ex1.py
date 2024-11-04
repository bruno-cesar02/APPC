import random
listaA = []
listaB = []
for i in range (100):
    numero_aleatorio = random.randint(-100, 100)
    if numero_aleatorio <= 0:
        listaB.append(numero_aleatorio)
    else: 
        listaA.append(numero_aleatorio)
print(f'Lista B : {listaB}')
print(f'lista A: {listaA}')