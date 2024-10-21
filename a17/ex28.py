for aluno in range(50):
    nome = input('digite seu nome:')
    nota1 = float(input('digite a nota 1: '))
    nota2 = float(input('digite a nota 2: '))
    nota3 = float(input('digite a nota 3: '))
    mediaponderada = (nota1 * 2 + nota2 * 4 + nota3*3)/10
    print(f'Nome do aluno : {nome}')
    print(f'Media Ponderada: {mediaponderada:.2f}')