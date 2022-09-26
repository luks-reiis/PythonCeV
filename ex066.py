print('='*40)
print('{:^40}'.format('Vários números com Flag'))
print('='*40)
count = soma = 0
while True:
    num = int(input('Digite um número inteiro (999 para parar): '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'Foram digitados {count} números e a soma entre eles é {soma}.')
