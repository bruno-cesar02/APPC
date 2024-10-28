import random
listaA = []
listaB = []
for i in range (100):
    numero_aleatorio = random.randint(-100, 100)
    listaA.append(numero_aleatorio)
for i in range(len(listaA)):
    if listaA[i] <=0:
        listaB.append(i)
        del listaA[i]
print(f'Lista B : {listaB}')
print(f'lista A: {listaA}')