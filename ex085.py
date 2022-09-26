print('='*40)
print(f'{"Lista composta com pares e ímpares":^40}')
print('='*40)
num = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número inteiro: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print('='*40)
print(f'Os valores pares digitados foram: {sorted(num[0])}.')
print(f'Os valores ímpares digitados foram: {sorted(num[1])}.')
