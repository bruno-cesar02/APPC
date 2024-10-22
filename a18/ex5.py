valortotal = 0
totalcomprado = 0
while True:
    codigo = int(input("Digite o codigo: "))
    if codigo == 0:
        break
    
    elif codigo == 1:
      preco = 0.50 
      qtde_comprada = int(input("digite a quantidade comprada: "))
      valortotal += qtde_comprada * preco
      totalcomprado+=qtde_comprada
      
    elif codigo == 2:
       preco = 1.00 
       qtde_comprada = int(input("digite a quantidade comprada: "))
       valortotal += qtde_comprada * preco
       totalcomprado+=qtde_comprada
       
    elif codigo == 3:
        preco = 4.00
        qtde_comprada = int(input("digite a quantidade comprada: "))
        valortotal += qtde_comprada * preco
        totalcomprado+=qtde_comprada
        
    elif codigo == 5:
        preco = 7.00
        qtde_comprada = int(input("digite a quantidade comprada: "))
        valortotal += qtde_comprada * preco
        totalcomprado+=qtde_comprada
        
    elif codigo == 9:
        preco= 8.00
        qtde_comprada = int(input("digite a quantidade comprada: "))
        valortotal += qtde_comprada * preco
        totalcomprado+=qtde_comprada
        
    else:
        print('Codigo Invalido')
print(f'Quantidade Comprada: {totalcomprado}')
print(f'Valor total : {valortotal:.2f}')