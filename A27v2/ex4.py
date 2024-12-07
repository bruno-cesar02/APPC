def validar_string(string,numeromin,numeromax):
    tamanhostr = len(string)
    if tamanhostr <= numeromax and tamanhostr >= numeromin:
        return True
    else:
        return False

string = input()
numeromin = int(input())
numeromax = int(input())
print(validar_string(string,numeromin,numeromax))