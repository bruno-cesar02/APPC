nota1 = float(input('digite a nota do aluno: '))
nota2 = float(input('digite a outra nota: '))
media = (nota1 + nota2)/2
if media >= 10:
   print('Aprovado com Distinção')
elif media >= 7:
   print('Aprovado')
else:
 print('Reprovado')