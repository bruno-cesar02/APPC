valorhora = float(input('Digite qnt voce ganha por hora: '))
horastrabalhadas = int(input('digite quantas horas voce trabalhou por mes: '))
salariobruto = valorhora * horastrabalhadas

valorfgts = salariobruto * (11/100)
valorinss = salariobruto * (10/100)
if salariobruto <= 900:
    
    totaldesconto = valorinss
    
    salarioliqui = salariobruto - totaldesconto
    
    print(f'Salario Bruto: {salariobruto:.2f} R$')
    print('IR : 00,00 R$')
    print(f'INSS: {valorinss}')
    print(f'FGTS: {valorfgts:.2f} R$')
    print(f'Total de Descontos: {totaldesconto:.2f}')
    print(f'Salario Liquido: {salarioliqui:.2f}')
elif salariobruto <= 1500:
    
    ir = salariobruto * (5/100)
    
    totaldesconto = valorinss + ir
    
    salarioliqui = salariobruto - totaldesconto

    print(f'Salario Bruto: {salariobruto:.2f} R$')
    print(f'IR : {ir:.2f} R$')
    print(f'INSS: {valorinss}')
    print(f'FGTS: {valorfgts:.2f} R$')
    print(f'Total de Descontos: {totaldesconto:.2f}')
    print(f'Salario Liquido: {salarioliqui:.2f}')
elif salariobruto <= 2500:
    
    ir = salariobruto *(10/100)
    
    totaldesconto = valorinss + ir
    
    salarioliqui = salariobruto - totaldesconto
    
    print(f'Salario Bruto: {salariobruto:.2f} R$')
    print(f'IR : {ir:.2f} R$')
    print(f'INSS: {valorinss}')
    print(f'FGTS: {valorfgts:.2f} R$')
    print(f'Total de Descontos: {totaldesconto:.2f}')
    print(f'Salario Liquido: {salarioliqui:.2f}')
else:
    ir = salariobruto *(20/100) 
    
    totaldesconto = valorinss + ir
    
    salarioliqui = salariobruto - totaldesconto
    
    print(f'Salario Bruto: {salariobruto:.2f} R$')
    print(f'IR : {ir:.2f} R$')
    print(f'INSS: {valorinss}')
    print(f'FGTS: {valorfgts:.2f} R$')
    print(f'Total de Descontos: {totaldesconto:.2f}')
    print(f'Salario Liquido: {salarioliqui:.2f}')