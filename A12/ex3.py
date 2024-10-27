idadehomem1 = int(input("Digite a idade para o primeiro homem: "))
idadehomem2 = int(input("Digite a idade para o segundo homem: "))
idademulher1 = int(input("Digite a idade para a primeira mulher: "))
idademulher2 = int(input("Digite a idade para a segunda mulher: "))
idadeHmaior = idadehomem1
idadeMmaior = idademulher1
if idadehomem2 > idadeHmaior:
    idadeHmaior = idadehomem2
    idadeHmenor = idadehomem1
    
if idademulher2 > idadeMmaior:
    idadeMmaior = idademulher2
    idadeMmenor = idadehomem1
print(f'soma das idades homem velho e nulher nova: {idadeHmaior+idadeMmenor}')
print(f'produto da idade do homem mais novo com a mulher mais velha: {idadeHmenor* idadeMmaior}')