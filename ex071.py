print('—'*40)
print('{:^40}'.format('Caixa Eletrônico'))
print('—'*40)
while True:
    print('$'*40)
    print(''' Notas disponíveis:
- R$50.00
- R$20.00
- R$10.00
- R$1.00''')
    print('$'*40)
    valor = int(input('Informe o valor a ser sacado: R$'))
    nota50 = valor // 50
    resto50 = valor % 50
    nota20 = resto50 // 20
    resto20 = resto50 % 20
    nota10 = resto20 // 10
    resto10 = resto20 % 10
    nota1 = resto10 // 1
    break
print('—'*40)
print('Será sacado:')
if nota50 > 0:
    print(f'- {nota50} cédulas de R$50.00.')
if nota20 > 0:
    print(f'- {nota20} cédulas de R$20.00.')
if nota10 > 0:
    print(f'- {nota10} cédulas de R$10.00.')
if nota1 > 0:
    print(f'- {nota1} cédulas de R$1.00.')
print('—'*40)