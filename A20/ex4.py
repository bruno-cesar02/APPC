lista = [1,2,3,4,5]
encontrou = False
procurar = int(input('Digite o elemento que deseja buscar:'))
for i in range (len(lista)):
    if lista[i] == procurar:
        print(f'Elemento encontrado na posicao : {i}')
        encontrou = True
if encontrou == False:
    print('Elemento nao encontrado')
    
