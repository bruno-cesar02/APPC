import math

# Programa para calcular a quantidade de latas de tinta e o preço total

# Variáveis de entrada
area = float(input("Informe o tamanho da área em metros quadrados a ser pintada: "))

# Cobertura da tinta (1 litro para cada 3 metros quadrados)
litros_necessarios = area / 3

# Cada lata tem 18 litros
latas_necessarias = math.ceil(litros_necessarios / 18)

# Preço de cada lata
preco_lata = 80.00

# Cálculo do preço total
preco_total = latas_necessarias * preco_lata

# Exibir resultados
print(f"Quantidade de latas necessárias: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")
