litros = int(input('Digite os litros vendidos'))
tipo = input('Digite o tipo do combustivel (A - alcool ou G - Gasolina)')
if tipo == 'A':
    if litros > 0 and litros <=20:
       print(f'Voce vai pagar {(litros*2.90) - (litros * 0.03)}')
    elif litros > 20:
       print(f'Voce vai pagar {(litros*2.90) - (litros * 0.05)}')
elif tipo == 'G':
    if litros > 0 and litros <=20:
       print(f'Voce vai pagar {(litros*3.30) - (litros * 0.04)}')
    elif litros > 20:
       print(f'Voce vai pagar {(litros*3.30) - (litros * 0.06)}')