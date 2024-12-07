def retirar_vogal(string):
    nova_string = ''
    for i in range(len(string)):
       if string[i] == 'a'or string[i] == 'e'or string[i] == 'i'or string[i] == 'o'or string[i] == 'u':
        print(end='')
       else:  
           nova_string += string[i]
    return nova_string


string = input('Digite a string: ').lower()
print(f'String sem as vogais: {retirar_vogal(string)}')
