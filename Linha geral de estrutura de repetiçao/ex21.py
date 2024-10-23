num1 = int(input("Digite um numero maior que zero: "))
num2 = int(input("Digite um numero maior que zero e maior q o numero anterior: "))
if num1 > 0 and num2 > 0 and num2 > num1:
    for i in range(num1,num2+1):
        print(f'Tabuada do {i}')
        for j in range(11):
            print(f'{i} X {j} = {i*j}')
else:
    print('Erro')