codigo = int(input('digite o codigo do aluno: '))
while codigo >0:
  nota1=float(input("digte a nota 1: "))
  nota2=float(input("digte a nota 2: "))
  nota3=float(input("digte a nota 3: "))
  if nota1 > nota2 and nota1 > nota3:
      media = ((nota1 * 4) + (nota2 * 3) + (nota3 * 3)) / 10
  elif nota2 > nota1 and nota2 > nota3:
     media = ((nota2 * 4) + (nota1* 3) + (nota3 * 3)) / 10
  elif nota3 > nota1 and nota3 > nota2:
      media = ((nota3 * 4) + (nota2 * 3) + (nota1 * 3)) / 10
  if media > 5:
        status = 'Aprovado'
  else:
        status = 'reprovado'
  print(f'codigo: {codigo}')
  print(f'nota 1: {nota1}')
  print(f'nota 2: {nota2}')
  print(f'nota 3: {nota3}')
  print(f'media: {media:.2f}')
  print(f'status: {status}')