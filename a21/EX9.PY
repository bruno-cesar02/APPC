conjunto1 = []
conjunto2 = []
intersecao = []
while True:
    n1 = int(input("Digite um numero para o conjunto1: (numero negativo para sair)"))
    n2 = int(input("Digite um numero para o conjunto2: (numero negativo para sair)"))
    if n1 < 0 or n2 < 0:
        break
    else:
        conjunto1.append(n1)
        conjunto2.append(n2)
for i in range(len(conjunto1)):
    if conjunto1[i] == conjunto2[i]:
        intersecao.append(conjunto1[i])
print(intersecao)
        