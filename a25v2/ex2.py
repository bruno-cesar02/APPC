nome = input("digite seu nome: ").upper()
nomemod = ""
for i in range(len(nome)-1,-1,-1):
    nomemod += nome[i]
print(nomemod)