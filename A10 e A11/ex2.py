valor1 = float(input('Digite um numero: '))
valor2 = float(input('Digite um numero: '))
valor3 = float(input('Digite um numero: '))
maior = valor1
menor = valor1
if valor2 >= maior:
    maior = valor2
if valor3 >= maior:
    maior = valor3
if valor2 <= menor:
    menor = valor2
if valor3 <= menor:
    menor = valor3
print(f'Esse foi o maior numero digitado: {maior}\nEsse foi o menor numero digitado: {menor}')