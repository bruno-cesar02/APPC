p1 = input().lower()
p2 = input().lower()
comparacao = True
if len(p1) == len(p2):
 for i in range(len(p1)):
    if p1[i] == p2[i]:
       comparacao = True
    else:
       comparacao = False
       break
 if comparacao == True:
    print("Palavras Iguais")
 elif comparacao == False:
    print("Palavras Diferentes")