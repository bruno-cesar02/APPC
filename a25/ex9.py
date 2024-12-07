x =input('Digite algo: ')
string = ''
for i in range(len(x)):
    if x[i] == '0':
        string += '1'
    else:
        string += x[i]
print(string)

