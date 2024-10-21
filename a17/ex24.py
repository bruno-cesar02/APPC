numerolido=0
somarnumero =0
numeropar =0
numeroimpar = 0
somarpar =0
somarimpar = 0
numero = int(input("Digite um numero: "))
while numero != 0 and numero > 0:
        somarnumero+=numero
        numerolido +=1
        if numero % 2 ==0:
            numeropar +=1
            somarpar+=numero
        else:
            numeroimpar+=1
        numero = int(input("Digite um numero: "))
if numeropar > 0:        
 mediapar = somarpar/numeropar
else:
    mediapar = 0

if numerolido > 0: 
 medianumerolido = somarnumero/numerolido
else:
    medianumerolido = 0
print(f'Numeros pares : {numeropar}')
print(f'Numeros impares : {numeroimpar}')
print(f' média de valores pares : {mediapar:.2f}')
print(f' média de valores lidos : {medianumerolido:.2f}')
            