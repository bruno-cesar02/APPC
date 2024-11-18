def somar_argumento (arg1,arg2,arg3):
    
    soma = arg1 + arg2 + arg3
    return soma
arg1 = float(input("Digite o argumento 1: "))
arg2 = float(input("Digite o argumento 2: "))
arg3 = float(input("Digite o argumento 3: "))
x = somar_argumento(arg1,arg2,arg3)
print(x)