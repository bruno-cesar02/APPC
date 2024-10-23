numero = int(input("digite o numero: "))
if numero <= 1:
    print('Nao é primo')
else:
    primo = True
    for i in range(2,numero):