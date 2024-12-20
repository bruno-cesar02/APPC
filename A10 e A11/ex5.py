''' 5. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma
ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo
grau e o programa não deve pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao
usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário; ''' 
a = float(input("digite o valor a: "))
if a != 0:
  b = float(input("digite o valor b: "))
  c = float(input("digite o valor c: "))
  delta = b**2 -4*a*c
  if delta <0:
      print('Delta calculado é negativo, a equação não possui raízes reais.')
  elif delta == 0:
        raiz = -b / (2 * a)
        print(f"A equação possui apenas uma raiz real: {raiz}")
  else:
        raiz1 = (-b + (delta ** 0.5)) / (2 * a)
        raiz2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")
else:
 print('Não é do segundo grau')