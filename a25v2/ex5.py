data_nasc = input("Digite a data:  (dd/mm/aaaa)")
mesnasc = data_nasc[3:5]
mes = ''
ano_nasc = data_nasc[6:]
dianasc = data_nasc[0:2]

if mesnasc == '01':
    mes += 'Janeiro'
    
elif mesnasc == '02':
    mes += 'Fevereiro'
    
elif mesnasc == '03':
    mes += 'Março'
    
elif mesnasc == '04':
    mes += 'Abril'
    
elif mesnasc == '05':
    mes += 'Maio'
    
elif mesnasc == '06':
    mes += 'Junho'
    
elif mesnasc == '07':
    mes += 'Julho'
    
elif mesnasc == '08':
    mes += 'Agosto'
    
elif mesnasc == '09':
    mes += 'Setembro'
    
elif mesnasc == '10':
    mes += 'Outubro'
    
elif mesnasc == '11':
    mes += 'Novembro'
    
elif mesnasc == '12':
    mes += 'Dezembro'

print(f'Você nasceu em {dianasc} de {mes} de {ano_nasc}.')