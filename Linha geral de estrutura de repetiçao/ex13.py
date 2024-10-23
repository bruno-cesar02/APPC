turmas = int(input('Entre com a quantidade de turmas: '))

soma_alunos = 0

for i in range(turmas):
    qtd_alunos = int(input('Entre com a quantidade de alunos: '))
    
    if qtd_alunos > 40:
        print('Excedeu o limite de alunos.')

    soma_alunos += qtd_alunos

media = soma_alunos / turmas
print(f'Média de alunos: {media}')