ganhahora = float(input('Quanto vc ganha por hora? '))
horastrabalhadas = int(input('digite as horas trabalhadas no mês :'))
salariobruto = ganhahora * horastrabalhadas
salariodpsdoimposto = salariobruto - (salariobruto *(11/100))
x = salariodpsdoimposto - (salariodpsdoimposto * 8/100)
valorinss = salariodpsdoimposto - x
a = valorinss - (valorinss * 5/100)
valorsindicato = valorinss - a
liquido = salariobruto - (salariobruto * 24/100)






print(f'este é seu salario bruto no referido mes: {salariobruto:.2f}R$')
print(f'voce pagou {valorinss:.2f} R$ para o INSS')
print(f'voce pagou {valorsindicato:.2f} R$ para o SINDICATO')
print(f'este é seu salario liquido: {liquido:.2f}R$')

