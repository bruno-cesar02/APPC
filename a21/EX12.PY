import random 
dado = [1,2,3,4,5,6]
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0

for i in range(100):
    x = random.randint(1,6)
    if x == dado[0]:
        cont1+= 1
    elif x == dado[1]:
        cont2 += 1
    elif x == dado[2]:
        cont3+= 1
    elif x == dado[3]:
        cont4 += 1
    elif x == dado[4]:
        cont5+= 1
    elif x == dado[5]:
        cont6+= 1
print(f'o numero 1 apareceu {cont1} vezes\no numero 2 apareceu {cont2} vezes\no numero 3 apareceu {cont3} vezes\no numero 4 apareceu {cont4} vezes\no numero 5 apareceu {cont5} vezes\no numero 6 apareceu {cont6} vezes')