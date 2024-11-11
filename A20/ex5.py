t  = [ -10, -8, 0, 1, 2, 5,-2, -4]
maiortemp = 0
menortemp = 0
for i in range(len(t)):
    if menortemp >= t[i]:
        menortemp = t[i]
    if maiortemp <= t[i]:
        maiortemp = t[i]
print(maiortemp,menortemp)
    