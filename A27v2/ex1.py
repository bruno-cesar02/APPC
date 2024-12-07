
def retornar_maior(n1,n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return n1

n1 = int(input())
n2 = int(input())
print(f'Máximo({n1},{n2}) == {retornar_maior(n1,n2)}')