print('='*30)
print('{:^30}'.format('Soma de pares'))
print('='*30)
soma = 0
count = 0
for c in range(0,5):
    num = int(input('Digite um número inteiro: '))
    if num %2 == 0:
        soma += num
        count += 1
print('A soma dos {} números pares é igual a {}.'.format(count, soma))