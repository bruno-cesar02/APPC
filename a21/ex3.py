consoantecont = 0 
lista = []
for i in range(10):
    letra = input("Digite uma letra:")
    lista.append(letra)
    if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u' and letra != 'A' and letra != 'E' and letra != 'I' and letra != 'O' and letra != 'U':
        consoantecont += 1
print(f'Lista: {lista}')
print(f'consoantes digitadas: {consoantecont}')