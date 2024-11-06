contador = 0
somanota = 0
notas = []
while True: 
    nota = input("Digite a nota : (digite sair para sair) ").lower()
    if nota == 'sair':
        print('saindo...')
        break
    else:
        nota = float(nota)
        somanota += nota
        notas.append(nota)
        contador+=1
print(f'A media das notas foi : {somanota/contador}')
print(f'Essas foram as notas digitadas: {notas}')