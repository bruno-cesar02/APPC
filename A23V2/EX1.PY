def ocorreu ():
    lista = []
    n = int(input())
    for i in range(n):
        x = float(input())
        lista.append(x)
    
    for i in range(len(lista)):
        cont=0
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                cont+=1
        if cont > 1:
         print(f'{lista[i]} ocorreu {cont} vezes')
        else:
            print(f'{lista[i]} ocorreu {cont} vez')
            
ocorreu ()
