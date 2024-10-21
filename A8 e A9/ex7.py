salarioantigo = float(input('digite seu salario: '))
if salarioantigo <= 280:
    salarionovo = salarioantigo + (salarioantigo*20/100)
    valoraumento= salarioantigo *20/100
    print(f'salário antes do reajuste : {salarioantigo:.2f} R$')
    print(f'percentual de aumento aplicado: 20% ')
    print(f'valor do aumento: {valoraumento:.2f} R$ ')
    print(f'novo salário, após o aumento: {salarionovo} R$')
    
elif salarioantigo > 280 and salarioantigo <=700:
    salarionovo = salarioantigo + (salarioantigo*15/100)
    valoraumento= salarioantigo *15/100
    print(f'salário antes do reajuste : {salarioantigo:.2f} R$')
    print(f'percentual de aumento aplicado: 15% ')
    print(f'valor do aumento: {valoraumento:.2f} R$ ')
    print(f'novo salário, após o aumento: {salarionovo} R$')
    
elif salarioantigo > 700 and salarioantigo <=1500:
    salarionovo = salarioantigo + (salarioantigo*10/100)
    valoraumento= salarioantigo *10/100
    print(f'salário antes do reajuste : {salarioantigo:.2f} R$')
    print(f'percentual de aumento aplicado: 10% ')
    print(f'valor do aumento: {valoraumento:.2f} R$ ')
    print(f'novo salário, após o aumento: {salarionovo} R$')
    
else:
    salarionovo = salarioantigo + (salarioantigo*5/100)
    valoraumento= salarioantigo *5/100
    print(f'salário antes do reajuste : {salarioantigo:.2f} R$')
    print(f'percentual de aumento aplicado: 5% ')
    print(f'valor do aumento: {valoraumento:.2f} R$ ')
    print(f'novo salário, após o aumento: {salarionovo} R$')