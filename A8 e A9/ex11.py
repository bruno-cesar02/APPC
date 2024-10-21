genero = input('Digite F - Feminino ou M - Masculino : ')
idade = int(input('Digite sua idade: '))
tempo = int(input("Digite seu tempo de contribuição: "))
if  genero == 'M':
    if idade >= 65 and tempo >=10:
        print("Aposentável")
    elif idade >= 63 and tempo >=15:
        print("Aposentável")
    else:
        print('Não Aposentável')
elif genero == 'F':
    if idade >= 63 and tempo >= 10:
        print("Aposentável")
    elif idade >= 61 and tempo >=15:
        print("Aposentável")
    else:
      print('Não Aposentável')
else:
 print("Genero Invalido")