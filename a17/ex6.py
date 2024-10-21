maior = float(input('Digite um numero: '))
for i in range(4):
    n = float(input('Digite um numero: '))
    if n > maior:
        maior = n
print(f'Esse foi o maior numero: {maior}')