def inverter_palavra (palavra):
     invertida = ''
     for i in range (len(palavra)-1,-1,-1):
        invertida += palavra[i]
     return invertida 

def verificar_palindromo(palavra):
    palavra_invertida = inverter_palavra(palavra).lower()
    for i in range(len(palavra)):
        if palavra[i] == palavra_invertida[i]:
            palindromo = True
        else:
            palindromo = False
    return palindromo
  
palavra = input('digite a palavra: ').lower()
if verificar_palindromo(palavra) == True:
    print('é palindromo')
else:
    print('Nao é palindromo')
        