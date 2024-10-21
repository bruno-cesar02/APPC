peso = float(input("digite o peso: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso*4
    
print(f'vc vai pagar {multa:.2f}R$ de multa ')