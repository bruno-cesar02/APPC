cont = 0
def contagem(frase,caractere,cont):
    for i in range(len(frase)):
        if frase[i] == caractere:
            cont += 1
    return cont
frase = input('Digite uma frase: ').lower()
caractere = input('Digite o caractere que deseja pesquisar: ').lower()

print(f'o caracter {caractere} aparece {contagem(frase,caractere,cont)} vezes na frase')
    