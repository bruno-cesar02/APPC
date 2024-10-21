somasalario =0
pessoasparticipantes = 0
maioridade = 0
mulhersalario = 0
while True:
    idade = int(input("Digite a idade: "))
    
    if idade <= 0:
        break
    else:
        menoridade = idade
        if idade < menoridade:
            menoridade = idade
        if idade > maioridade:
            maioridade = idade
        sexo = input("digite o sexo (M - Masculino, F - Feminino)")
        salario = float(input("Digite o salario: "))
        somasalario +=salario
        pessoasparticipantes +=1
        if sexo == 'F' and salario <=100:
            mulhersalario +=1
if pessoasparticipantes >0 and somasalario > 0:
 mediasalariogrupo = somasalario/pessoasparticipantes
else:
    mediasalariogrupo = 0
print(f'a média de salário do grupo: {mediasalariogrupo:.2f} R$')
print(f'maior idade do grupo: {maioridade}')
print(f'menor idade do grupo: {menoridade}')
print(f'quantidade de mulheres com salário até R$100,00 : {mulhersalario}')
    