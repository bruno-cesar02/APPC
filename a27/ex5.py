def somaImposto (taxaImposto,custo):
       taxa_imposto = taxa/100
       custo = preco_item + (preco_item*taxa_imposto)
       return custo
preco_item = float(input("digite o preco do item: "))
taxa = int(input("Digite o valor da taxa. ex(5 para 5%) : " ))
x = somaImposto(taxa,preco_item)
print(x)