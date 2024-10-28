lista = []
while True:
    n = float(input("Digite um numero:"))
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
    elem = input('Digite o elemento que deseja buscar : ')
    encontrou = False
    for i in range(len(lista)):
        if lista[i] == elem:
            print('Elemento encontrado')
            encontrou = True
            break
    if encontrou == False:
     print('elemento nao encontrado')