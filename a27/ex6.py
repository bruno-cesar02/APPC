def converter_horas (horas, minutos):
      if horas == 0:
         return 12, minutos,'A.M'
           
      elif horas >= 1 and horas <=11:
           return horas,minutos,'A.M'
      elif horas > 12 and horas <= 23:
           return horas - 12,minutos,'P.M'
def imprimir (horas,minutos,periodo):
     print(f'{horas}:{minutos} {periodo}')

while True:
    horas = int(input("digite as horas: "))
    minutos = int(input("digite os minutos: "))
    if horas >= 0 and horas <= 23 and minutos >= 0 and minutos <= 59:
        horas,minutos,periodo = converter_horas(horas,minutos)
        imprimir(horas,minutos,periodo)
    else:
        print("horas ou minutos invalidas")
    opc = input("digite sair para encerrar o programa: ").lower()
    if opc == 'sair':
        break
