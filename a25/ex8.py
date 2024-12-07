cont = 0
x = int(input('Digite um numero: '))
x = str(x)
for i in range (len(x)):
    if x[i] == '1':
        cont += 1
print(f'Quantidade de 1: {cont}')