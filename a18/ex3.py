somatotal=0

while True:
      somavalor=0
      while True: 
         preco = float(input("digite o preço do produto: "))
         somavalor += preco
         somatotal += somavalor
         print('Ainda ha itens para serem lidos: ')
         opc = input("digite S para Sim e N para Não")
         if opc == 'N':
            break
       
      print(f'Sua compra custou: {somavalor:.2f} R$')
      fecharcaixa=input('Deseja fechar o caixa ? S para Sim e N para Não')
      if fecharcaixa == 'S':
         print("fechando caixa...")
         break
   
print(f'esse foi o valor apurado nesse dia : {somatotal:.2f}')
        