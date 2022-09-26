print('='*30)
print('{:^30}'.format('Números Primos'))
print('='*30)
num = int(input('Digite um número inteiro:'))
div = 0
print('\nOs divisores de {} são:\n'.format(num))
for c in range(1, num+1):
    if num %c == 0:
        div += 1
        print(c)
if div <= 2:
    print ('\n{} é primo, pois possui {} divisores.'.format(num, div))
else:
    print ('\n{} não é primo, pois possui {} divisores.'.format(num, div))