n = int(input("digite um numero"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i == j:
            print(j)
        else:
            print(' ',end='')