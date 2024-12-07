lista = []
listanova = []
while True:
    n = int(input("Digite um numero:"))
    lista.append(n)
    opc = input('deseja inserir outro valor: (n - nao, s - sim)')
    if opc == 'n':
        break
print(lista)
##################
while True:
    opc = input("deseja buscar elemento na lista? (s/n) ")
    if opc == 'n':
        break
    elem = int(input('Digite o elemento que deseja buscar : '))
    encontrou = False
    for i in range(len(lista)):
        if lista[i] == elem:
            print('Elemento encontrado')
            listanova.append(lista[i])
            del lista[i]
            encontrou = True
            print(listanova)
            print(lista)
            break
    if encontrou == False:
     print('elemento nao encontrado')
