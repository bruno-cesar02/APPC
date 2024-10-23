totalvalorgeral = 0
while True:
    codigo = int(input('Digite o codigo: '))
    qtde = int(input('Digite a quantidade: '))
    if codigo == 100:
        valortotal = qtde * 1.20
        totalvalorgeral+= valortotal
        print(f'Voce vai pagar {valortotal:.2f} R$ ')
        
    elif codigo == 101:
        valortotal = qtde * 1.30
        totalvalorgeral+= valortotal
        print(f'Voce vai pagar {valortotal:.2f} R$ ')
        
    elif codigo == 102:
        valortotal = qtde * 1.50
        totalvalorgeral+= valortotal
        print(f'Voce vai pagar {valortotal:.2f} R$ ')
        
    elif codigo == 103:
        valortotal = qtde * 1.20
        totalvalorgeral+= valortotal
        print(f'Voce vai pagar {valortotal:.2f} R$ ')
        
    elif codigo == 104:
        valortotal = qtde * 1.30
        totalvalorgeral+= valortotal
        print(f'Voce vai pagar {valortotal:.2f} R$ ')
        
    elif codigo == 105:
        valortotal = qtde * 1.00
        totalvalorgeral+= valortotal
        print(f'Voce vai pagar {valortotal:.2f} R$ ')
    opc = input("Digite 'fechar' para sair ou qualquer coisa para continuar.")
    if opc == 'fechar':
        break
print(f'Voce vai pagar: {totalvalorgeral:.2f} R$ no geral')
            