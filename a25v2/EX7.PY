string1 = input()
string2 = input()
resultado = ''
for char in string1:
    if char in string2:
        resultado += char
        string2 = string2.replace(char,'')
print(resultado)

