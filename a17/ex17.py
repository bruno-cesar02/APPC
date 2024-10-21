bom = 0
regular = 0
otimo = 0
somaidade = 0
for i in range(15):
    idade = int(input("Digite a idade: "))
    opn = input("digite sua opnião (3-otimo, 2-bom, 1-regular): ")
    if opn == '3':
        somaidade+= idade
        otimo+=1
    elif opn == '1':
        regular += 1
    elif opn == '2':
        bom +=1
mediaidade = somaidade/otimo
porcentagem = (bom/15)*100

print(f'A media das idades : {mediaidade}')
print(f'pessoas que votaram regular: {regular}')
print(f'Porcentagem de pessoas q votaram bom: {porcentagem:.2f} %')