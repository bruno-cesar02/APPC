nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 9 and media <=10:
    conceito = 'A'
elif media >= 7.5 and media < 9:
    conceito = 'B'
elif media >= 6.0 and media <=7.5:
    conceito = 'C'
elif media >= 4.0 and media <=6.0:
    conceito = 'D'
elif media <= 4.0 and media >=0:
    conceito = 'E'



if conceito == 'A':
    situacão = 'Aprovado'
elif conceito == 'B':
    situacão = 'Aprovado'
elif conceito == 'C':
    situacão = 'Aprovado'
elif conceito == 'D':
    situacão = 'Reprovado'
elif conceito == 'E':
    situacão = 'Reprovado'
print(f'nota 1 : {nota1}\nnota 2 : {nota2}\nmedia : {media}\nconceito : {conceito}\nSituação: {situacão}')