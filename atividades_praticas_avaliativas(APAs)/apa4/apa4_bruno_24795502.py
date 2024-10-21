###################################################
# PUC - CAMPINAS
# Prof. Msc. Luã Marcelo Muriana
# Algoritmos de Programação, Projetos e Computação
# Engenharia de Software 2024/2
# Atividade Prática 4 - Jornada de Trabalho
# Nome: Bruno César Gonçalves Lima Mota
# RA: 24795502
###################################################
v = int(input())
d = int(input())
total_horas = 0
total_horas_extras = 0
total_horas_trabalhadas = 0
for dia in range(d):
    numero_periodo = int(input())
    
    horas_dia = 0 # horas trabalhadas no dia
    for periodo in range(numero_periodo):
        hora_inicio = int(input())
        hora_fim = int(input())
        
        # Calculando o tempo trabalhado no período
        horas_trabalhadas = hora_fim - hora_inicio
        horas_dia += horas_trabalhadas
    total_horas_trabalhadas += horas_dia
        
    if horas_dia > 8:
        horas_extras_dia = horas_dia - 8
        total_horas_extras += horas_extras_dia
        total_horas += 8
    else:
        total_horas += horas_dia
        
if total_horas > 44:
    horas_extra_semanal = total_horas - 44
    total_horas_extras += horas_extra_semanal
    total_horas = 44  # Ajusta o total de horas normais para o limite de 44
    
valornormal = total_horas * v
valorextra = total_horas_extras * (v * 1.5)
valor_total = valornormal + valorextra

print(f'Horas trabalhadas: {total_horas_trabalhadas}')
print(f'Horas extras: {total_horas_extras}')
print(f'Valor devido: R$ {valor_total:.2f}')