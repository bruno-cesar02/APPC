Primeirasequência=[1,1, 3, 5, 5, 7, 9, 10, ] 
Segundasequência= [2, 2, 4, 6, 8, 8, 10] 
listaordenada = []
i = 0
j = 0
while i < len(Primeirasequência) and j < len(Segundasequência) :
    if Primeirasequência[i] < Segundasequência[j] :
         listaordenada.append(Primeirasequência[i])
         i += 1 
    else:
        listaordenada.append(Segundasequência[j])
        j += 1
# Adiciona os elementos restantes da sequencia1, se houver
while i < len(Primeirasequência):
    listaordenada.append(Primeirasequência[i])
    i += 1

# Adiciona os elementos restantes da sequencia2, se houver
while j < len(Segundasequência):
    listaordenada.append(Segundasequência[j])
    j += 1


print(f"Resultado:{listaordenada}")



        
                    
                
   
