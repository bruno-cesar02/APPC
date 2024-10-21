n = int(input('Digite o numero: '))
fatorial = 1
print(f'{n}!=',end='')
for i in range(n,0,-1):
    print(i,end=' ')
    if i > 1:
     print('X',end=' ')
    fatorial *= i
print(f'= {fatorial}')
    