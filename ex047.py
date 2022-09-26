print('='*30)
print('{:^30}'.format('Contagem de números pares'))
print('='*30)
print('Abaixo estão todos os números pares que estão contidos num intervalo de 1-50:')
for c in range(1,51):
    if c %2 == 0:
        print(c)
