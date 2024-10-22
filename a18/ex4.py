numerosdigitados = 0
soma=0
while True:
    n = int(input("digite um numero (digite 0 para encerrar)"))
    if n == 0:
        break
    else:
        numerosdigitados+=1
        soma+=n 
if soma > 0:
    mediaaritimetica = soma/numerosdigitados
else:
    mediaaritimetica = 0
print(f'numeros digitados: {numerosdigitados}')
print(f'Soma: {soma}')
print(f'Media Aritimrtica : {mediaaritimetica:.2f}')
    