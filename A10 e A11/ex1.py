
maior = float(input('Digite um numero: '))
valor1 = float(input('Digite um numero: '))
valor2 = float(input('Digite um numero: '))
if maior <= valor1:
    maior = valor1
if maior <= valor2:
    maior = valor2
print(f'Esse foi o maior numero digitado: {maior}')