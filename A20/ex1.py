contador = 0
somanota = 0
notas = []
qtde_notas = int(input("Digite a quantidade de notas: "))

for i in range(qtde_notas):
    nota = float(input("Digite a nota : "))
    somanota += nota
    notas.append(nota)
    contador+=1
print(f'A media das notas foi : {somanota/contador}')
print(f'Essas foram as notas digitadas: {notas}')