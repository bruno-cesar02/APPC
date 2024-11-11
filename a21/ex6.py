lista = []
pares = []
impares = []
for i in range(20):
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Lista pares: {pares}')
print(f'Lista impares: {impares} ')
print(f'Lista normal : {lista} ')