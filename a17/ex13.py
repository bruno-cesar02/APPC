entre0e100 = 0
entre101e200 = 0
maiorque200 = 0
for i in range(20):
    n = int(input("digite um numero: "))
    if n > 0 and n < 100:
        entre0e100 += 1 
    if n > 101 and n <200:
        entre101e200 += 1
    if n >200:
        maiorque200+=1
print(f'Entre 0 a 100 : {entre0e100}\nEntre 101 a 200: {entre101e200}\nMaior que 200:{maiorque200}')