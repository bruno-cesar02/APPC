temperaturames =[]
soma = 0
meses = ['janeiro','fevereiro','março','Abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
for i in range(12):
    temperatura = float(input('Digite a temperatura'))
    temperaturames.append(temperatura)
    soma+=temperatura
mediaanual = soma/12
for j in range(12): 
    if temperaturames[j] > mediaanual:
        print(f'A temperatura de {meses[j]} é maior que media anual pois a media é {mediaanual} e a temperatura desse mes é {temperaturames[j]}')