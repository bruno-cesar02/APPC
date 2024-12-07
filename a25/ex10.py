x =input('Digite algo: ').lower()
opc = input('Digite o que quer substituir: ').lower()
opc1 = input(f'o que deseja inserir no lugar de {opc}: ').lower()
string = ''
for i in range(len(x)):
    if x[i] == opc:
        string += opc1
    else:
        string += x[i]
print(string)

