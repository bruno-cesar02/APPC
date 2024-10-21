alunos = int(input('Quantos alunos tem na sala: '))

somamateria = 0
somanota =0

for aluno in range(1,alunos+1):
     print(f'Aluno {aluno}:')
     somanotaaluno=0
     materias = int(input("Quantas materias esse aluno estuda: "))
     for i in range(materias):
         nota = float(input(f"Digite a nota do aluno {aluno} : "))
         somanotaaluno += nota
         somanota+=nota
     print(f'media do aluno {aluno}: {somanotaaluno/materias:.2f} ')
print(f'Media da turma: {somanota/alunos:.2f}')