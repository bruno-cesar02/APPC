tipo = input('Digite o tipo dos Graus (F - fahrenheit ou C - Celsius): ')
if tipo == 'F':
    fahrenheit = float(input("Digite os Graus farenheit: "))
    grauconvertido = (fahrenheit - 32) * 5/9
    print(f'Esses é seus graus Farenheit convertido para celsius: {grauconvertido:.2f} C ')

elif tipo == 'C':
    celsius = float(input('Digite os graus Celsius: '))
    grauconvertido = celsius *(9/5) + 32
    print(f'Esses é seus graus Celsius convertido para Farenheit: {grauconvertido:.2f} F ')
else:
    print('Erro, digite o caracterer correto')