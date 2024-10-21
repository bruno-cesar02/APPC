n = int(input("Quantos valores você deseja ler? "))

for i in range(n):
    valor = int(input("Digite um número: "))
    fatorial = 1
    for i in range(1, valor + 1):
        fatorial *= i
    print(f"{valor}! = {fatorial}")
        