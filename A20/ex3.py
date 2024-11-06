lista1 = []
lista2 = []
lista3 = []
lista4 = []
numerolido = 0
while True:
    n = int(input('digite um numero: (digite um numero negativo para encerrar)'))
    if n < 0:
        break 
    elif n <=25:
        lista1.append(n)
    elif n <= 50:
        lista2.append(n)
    elif n <= 75:
        lista3.append(n)
    elif n > 75 and n <=100:
        lista4.append(n)
    numerolido+=1
print(f'lista1: {lista1}')
print(f'lista2: {lista2}')
print(f'lista3: {lista3}')
print(f'lista4: {lista4}')
print(f'foram lidos {numerolido} numeros')
'''
print(f'media da lista1: {sum(lista1)/len(lista1):.2f}')
print(f'media da lista2: {sum(lista2)/len(lista2):.2f}')
print(f'media da lista3: {sum(lista3)/len(lista3):.2f}')
print(f'media da lista4: {sum(lista4)/len(lista4):.2f}')
'''