''' 4. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o
mesmo é: equilátero, isósceles ou escaleno.
Dicas:
• Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
que o terceiro;
• Triângulo Equilátero: três lados iguais;
• Triângulo Isósceles: quaisquer dois lados iguais;
• Triângulo Escaleno: três lados diferentes;'''
lado1 = float(input("digite o lado 1 :"))
lado2 = float(input("digite o lado 2 :"))
lado3 = float(input("digite o lado 3 :"))  
if lado1 + lado2 > lado3 or lado2 + lado1 > lado3 : #ve se é triangulo
    print("é um triangulo")
    if lado1 == lado2 and lado2 == lado3:
        print("Triangulo equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('Triangulo isósceles')
    else:
     lado1 != lado2 and lado2 != lado3 and lado3 != lado1
     print('Triangulo Escaleno')
else:
 print('Não é um triangulo')