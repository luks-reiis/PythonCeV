from random import randint

print('=' * 40)
print('{:^40}'.format('Maior e Menor Valor com Tuplas'))
print('=' * 40)

sorte = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números sorteados foram:', end=' ')
count = 0
for num in sorte:
    print(num, end='   ')
print('')
print(f'O maior número sorteado foi {max(sorte)}.')
print(f'O menor número sorteado foi {min(sorte)}.')
