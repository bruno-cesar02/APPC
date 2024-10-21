'''
produto = 100
custo = produto * (70/100)
lucro = produto *(5/100)
imposto = produto *(10/100)

print(custo)'''


# Preço de venda inicial
preco_venda_inicial = 100

# Composição do preço inicial
custo_inicial = preco_venda_inicial * 0.60
lucro_inicial = preco_venda_inicial * 0.10
impostos_inicial = preco_venda_inicial * 0.30

# Aumento do custo
aumento_custo = custo_inicial * 0.10
novo_custo = custo_inicial + aumento_custo

# Redução dos impostos
reducao_impostos = impostos_inicial * 0.20
novos_impostos = impostos_inicial - reducao_impostos

# Redução do lucro
novo_lucro = lucro_inicial / 2

# Novo preço de venda
novo_preco_venda = novo_custo + novo_lucro + novos_impostos

# Impressão do resultado
print(f"O novo preço de venda do produto é R$ {novo_preco_venda:.2f}")
