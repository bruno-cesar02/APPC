
def imprimir_contrario(nome): 
 nomecontrario = ''
 for i in range(len(nome)-1,-1,-1):
     nomecontrario += nome[i]
 return nomecontrario
nome = input('Digite seu nome: ')
print(f'seu nome ao contrario é: {(imprimir_contrario(nome))}')