qtde_produtos = 0
somapreconormal=0
somapreconovo = 0
while True:
 codigo = int(input('Digite o codigo(digite um numero negativo para encerrar o programa): '))
 if codigo < 0:
     break
 else:
     precodecusto = float(input("Digite o preço do produto: "))
     preconovo = precodecusto + (precodecusto * 0.20)
     print(f'Codigo: {codigo}')
     print(f'Preço novo: {preconovo:.2f} R$')
     qtde_produtos +=1
     somapreconormal += precodecusto
     somapreconovo += preconovo
if somapreconormal >0:
    mediapreconormal = somapreconormal/qtde_produtos
else:
    mediapreconormal = 0
if somapreconovo > 0:
    mediapreconovo = somapreconovo/qtde_produtos
else:
    mediapreconovo = 0
print(f'media do preco antigo: {mediapreconormal:.2f} R$')
print(f'media do preco novo: {mediapreconovo:.2f} R$')