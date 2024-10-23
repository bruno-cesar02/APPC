salario_inicial = float(input("digite o salario inicial: "))
ano_contrataçao = 1995
ano_atual = 2024
percentual_aumento = 1.5
salarioatual = 0
salario = salario_inicial + (salario_inicial * percentual_aumento/100)

for i in range(1997,ano_atual + 1):
    percentual_aumento *= 2
    salarioatual += salario + (percentual_aumento/100)
print(f'O salario atual no ano de {ano_atual} é de {salarioatual:.2f} R$ ')