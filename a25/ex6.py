nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo: (F - Feminino ou M - Masculino): ').upper()
idade = int(input('Digite sua idade: '))
if sexo == 'F' and idade < 25:
    print(f'Nome: {nome}\n ACEITA')
else:
    print(f'Nome: {nome}\n NAO ACEITA')