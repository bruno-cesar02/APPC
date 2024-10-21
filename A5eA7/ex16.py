import math
area = float(input("digite os metros quadrados: "))
if area > 0:
   litros_necessarios = area/6
   litrofolga = litros_necessarios *1.1
   latas_necessarias = math.ceil(litrofolga/18)
   preco_lata= latas_necessarias*80

   galoes_necessarios = math.ceil(litrofolga/3.6)
   preco_galoes = galoes_necessarios*25

   lata_aproximada = int(litrofolga//18)
   restante_tinta = litrofolga - (lata_aproximada * 18)
   galoes_aproximados = math.ceil(restante_tinta/3.6)
   preco_misto = (lata_aproximada * 80) + (galoes_aproximados * 25)
   
   print("Apenas latas de 18 litros")
   print(f"Quantidade de latas: {latas_necessarias}")
   print(f"Preço total: R$ {preco_lata:.2f}")

   print("\nSituação 2: Apenas galões de 3,6 litros")
   print(f"Quantidade de galões: {galoes_necessarios}")
   print(f"Preço total: R$ {preco_galoes:.2f}")

   print("\nSituação 3: Mistura de latas e galões")
   print(f"Quantidade de latas: {lata_aproximada}")
   print(f"Quantidade de galões: {galoes_aproximados}")
   print(f"Preço total: R$ {preco_misto:.2f}")

   