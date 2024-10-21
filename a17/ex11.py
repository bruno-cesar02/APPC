'''
soma = 0
for i in range(10):
    n = int(input('digite um numero:'))
    soma += n

par = 0
impar = 0
for j in range(soma+1):
    if j % 2 == 0:
        par +=1
    else:
        impar += 1
print(f'Existem {par} numeros pares e {impar} numeros impares entre a soma dos numeros digitados')
'''
par = 0
impar = 0
for i in range(10):
    n = int(input("digite um numero: "))
    if n % 2 == 0:
        par +=1
    else:
        impar +=1
print(f'numeros pares: {par}\nnumeros Impares: {impar}')