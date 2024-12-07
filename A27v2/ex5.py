def valorPagamento (valor_prestacao,dias_atraso):
    if dias_atraso == 0:
        valor_pagar = valor_prestacao
        return valor_pagar
    else:
        multa = valor_prestacao * (0.03 + (0.001 * dias_atraso))
        valor_pagar = valor_prestacao + multa
        return valor_pagar
contpagas = 0
valortotal = 0    
    
while True:
  valor_prestacao = float(input('Digite o valor da prestacao: '))
  if valor_prestacao == 0.0:
     break
  dias_atraso = int(input('Digite os dias atrasados: '))
  print(f'Valor a pagar: R$ {valorPagamento(valor_prestacao,dias_atraso)}')
  contpagas +=1
  valortotal += valorPagamento(valor_prestacao,dias_atraso)
  
print(f'quantidade de contas pagas: {contpagas}\n Valor total : R$ {valortotal}')
