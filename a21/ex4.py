lista= []
soma =0
for i in range(10):
    n = int(input('Digite um numero: '))
    lista.append(n)
    x = n ** 2
    soma += x
print(f'Lista: {lista}')
print(f'Soma: {soma}')
    