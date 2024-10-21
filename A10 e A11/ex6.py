# Solicita ao usuário que insira um número inteiro menor que 1000
numero = int(input("Digite um número inteiro menor que 1000: "))

# Verifica se o número está no intervalo permitido
if numero >= 1000 or numero < 0:
    print("O número deve ser maior ou igual a 0 e menor que 1000.")
else:
    # Calcula as centenas, dezenas e unidades
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    # Constrói a saída de forma adequada com singular/plural
    resultado = ""

    # Verifica a quantidade de centenas
    if centenas > 0:
        if centenas == 1:
            resultado += f"{centenas} centena"
        else:
            resultado += f"{centenas} centenas"

    # Verifica a quantidade de dezenas
    if dezenas > 0:
        if resultado != "":
            resultado += ", "
        if dezenas == 1:
            resultado += f"{dezenas} dezena"
        else:
            resultado += f"{dezenas} dezenas"

    # Verifica a quantidade de unidades
    if unidades > 0:
        if resultado != "":
            resultado += " e "
        if unidades == 1:
            resultado += f"{unidades} unidade"
        else:
            resultado += f"{unidades} unidades"

    # Caso o número seja 0, há apenas 0 unidades
    if numero == 0:
        resultado = "0 unidades"

    # Exibe o resultado final
    print(resultado)
