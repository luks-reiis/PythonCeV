a=input('Digite algo:')
print('o tipo primitivo de {} é {}:'.format(a,type(a)))
print('{} só tem espaços?'.format(a),a.isspace())
print('{} é um número?'.format(a),a.isnumeric())
print('{} é alfabético?'.format(a),a.isalpha())
print('{} é alfanumérico?'.format(a),a.isalnum())
print('{} está em letras maiúsculas? (todas as letras)'.format(a),a.isupper())
print('{} está em letras minúsculas? (todas as letras)'.format(a),a.islower())
print('{} apresenta a primeira letra maiúscula e o restante em minúsculas?'.format(a),a.istitle())