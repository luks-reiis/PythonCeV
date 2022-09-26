print('='*40)
print(f'{"Extraindo Dados de Uma Lista":^40}')
print('='*40)
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] '))[0].strip().upper()
    if resp == 'N':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}.')
if 5 not in valores:
    print('O valor 5 não foi encotrado na lista!')
else:
    print(f'O valor 5 foi encontrado {valores.count(5)} vezes na lista!')