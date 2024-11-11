lista =[]
listainversa =[]
for i in range(10):
    n = int(input("digite um numero: "))
    lista.append(n)
for j in range(len(lista) -1,-1,-1):
    listainversa.append(lista[j])
print("a lista informada foi: ",lista)
print( listainversa)