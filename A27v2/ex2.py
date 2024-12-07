def verificar_multiplo (n1,n2):
    if n1 % n2 == 0:
        return True
    else:
        return False
n1 = int(input())
n2 = int(input())

print(f'Multiplo ({n1},{n2}) == {verificar_multiplo(n1,n2)}')