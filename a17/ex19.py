valorcarro = float(input("Digite o valor do carro : "))
print(f"Preço final à vista: R${valorcarro * 0.80:.2f}")

for parcelas in range(6, 61, 6):
    percentual = parcelas // 6 * 3
    preco_final = valorcarro * (1 + percentual / 100)
    valor_parcela = preco_final / parcelas
    print(f"{parcelas} parcelas: Preço final: R${preco_final:.2f}, Valor da parcela: R${valor_parcela:.2f}")