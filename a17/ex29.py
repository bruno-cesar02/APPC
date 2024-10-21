while True:
 print('1. Média aritmética') 
 print('2. Média ponderada')
 print('3. Sair')
 opc = int(input("Digite a opção: "))
 if opc == 3:
     break
 else:
     if opc == 1:
         nota1 = float(input("Digite a nota 1: "))
         nota2 = float(input("Digite a nota 2: "))
         mediaaritimetica = (nota1 + nota2 )/ 2
         print(f'media aritmetica das suas notas : {mediaaritimetica:.2f}')
     elif opc == 2:
         nota1 = float(input("Digite a nota 1: "))
         nota2 = float(input("Digite a nota 2: "))
         nota3 = float(input("Digite a nota 3: "))
         peso1 = int(input("Digite o peso 1 :"))
         peso2 = int(input("Digite o peso 2 :"))
         peso3 = int(input("Digite o peso 3 :"))
         mediaponderada = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1+peso2+peso3)
         print(f'Essa é sua media Ponderada: {mediaponderada:.2f}')
     else:
         print('Opção Invalida') 