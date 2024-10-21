
while True:
    num = int(input("Digite um numero: "))
    print('1 - adição')
    print('2 - subtração')
    print('3 - divisao')
    print('4 - multiplicao')
    print('0 - sair')
    opc = int(input("Digite o numero da opçao : "))
    if opc == 0:
        print("encerrando o programa!")
        break
    elif opc == 1:
       for i in range(1,11):
        print(f'{num} + {i} = {num+i}')
        
    elif opc == 2:
     for i in range(1,11):
      print(f'{num} - {i} = {num-i}')
      
    elif opc == 3:
     print(f'{num} / 0 = 0')
     for i in range(1,11):
      print(f'{num} / {i} = {num/i}')
      
    elif opc == 4:
     for i in range(1,11):
      print(f'{num} X {i} = {num*i}')