
while True:
    n = int(input("digite um valor: "))
    if n > 0:
        
      if n % 2 == 0: #verificar se é par 
         divisores = 0
         for i in range(1,n+1):
             
            if n % i == 0:
               divisores+=1
         print(f'{n} é par e esse é o tanto de divisores que {n} possui: {divisores}')
      elif n < 10:
          fatorial = 1
          print(f'{n}!=', end='')
          for i in range(n,1,-1):
              fatorial *= i
          print(f' {fatorial}')
      elif n >=10:
            soma = 0
            for i in range(1,n):
                soma+=i
            print(f'Essa é a soma de 1 até {n}: {soma}')              
    else:
      break