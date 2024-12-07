def pegar_nome(nome):
    if nome[0] == 'a':
        nome_verdadeiro = nome
        return nome_verdadeiro
    else:
        nome_verdadeiro = 'nome não começa com a letra a'
        return nome_verdadeiro
nome = input('Digite seu nome: ').lower()
print(pegar_nome(nome))