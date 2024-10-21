idadesuperior50 = 0
pessoaalturainferior = 1
somaidade = 0
ruivosemazul = 0
olhoazul = 0

for i in range(20):
    idade = int(input("digite a idade: "))
    peso = int(input("digite o peso: "))
    altura = float(input('digite a altura: '))
    corOlho = input('digite a cor do olho:  (A – Azul, P- Preto, V- Verde e C- Castanho)')
    corCabelo = input('digite a cor do cabelo: (P – Preto, C- Castanho, L – Louro e R-Ruivo)')
    if idade > 50 and peso <60:
      idadesuperior50 += 1
    if altura <1.50:
        somaidade+= idade
        pessoaalturainferior +=1
    if corOlho == 'A':
        olhoazul +=1
    if corCabelo == 'R' and corOlho != 'A':
        ruivosemazul+=1
if pessoaalturainferior > 0:
 mediaidade = somaidade/pessoaalturainferior
else:
    mediaidade =0
porcentagemolhoazul = (olhoazul / 20) * 100    
print(f'A quantidade de pessoas com idade superior a 50 anos e peso inferior a 60kg: {idadesuperior50}')
print(f'A média das idades das pessoas com altura inferior a 1,50: {mediaidade:.2f}')
print(f'A porcentagem de pessoas com olhos azuis entre as pessoas analisadas: {porcentagemolhoazul:.2f} %')
print(f'A quantidade de pessoas ruivas que não possuem olhos azuis: {ruivosemazul}')
        