import random

def advinhar():

    n = random.randit(1,10)
    tentativas = 3
    while tentativas > 0:
        x = int(input('Escolha um número entre 1 e 10: '))
        
        if (x == n):
         print('Você acertou!')
         break
        elif x != n:
          print('Você errou')
          tentativas -= 1
        if tentativas  == 0:
            print('Suas chances acabaram')

