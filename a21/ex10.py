conjunto1 = []
conjunto2 = []
intersecao = []
while True:
    n1 = int(input("Digite um numero para o conjunto1: (numero negativo para sair)"))
    n2 = int(input("Digite um numero para o conjunto2: (numero negativo para sair)"))
    if n1 < 0 or n2 < 0:
        break
    elif n1 != n2:
        conjunto1.append(n1)
        conjunto2.append(n2)
    else:
        print("os numeros precisam ser diferentes")
       
for i in range(len(conjunto1)):
    for j in range(len(conjunto2)):
        if conjunto1[i] == conjunto2[j]:
           if conjunto1[i] == intersecao[j]:
               print('ja esta na lista')    
           else:
               intersecao.append(conjunto1)