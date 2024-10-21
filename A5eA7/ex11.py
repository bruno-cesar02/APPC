num1 = int(input('entre com um numero'))
num2 = int(input('entre com outro numero'))
numreal = float(input('entre com outro numero'))

a = (num1 * 2) + (num2/2)
b = (num1 * 3) + numreal
c = numreal**3

print(f'produto do dobro do primeiro com metade do segundo:{a}')
print(f'a soma do triplo do primeiro com o terceiro:{b}')
print(f'o terceiro elevado ao cubo:{c}')