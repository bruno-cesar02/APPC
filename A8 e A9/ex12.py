num1 = float(input('Digite um numero: '))
num2 = float(input('Digite um numero: '))
opc = input('Digite o que deseja fazer: (+,-,/,x) ')
if opc == '+':
    print(num1 + num2)
elif opc == '-':
    print(num1 - num2)
elif opc == 'x':
    print(num1 * num2)
elif opc == '/':
    print(num1 / num2)
else:
    
    print('Invalido')