print('='*40)
print('{:^40}'.format('Fatorial de um Número'))
print('='*40)
num = int(input('Digite um número inteiro e maior do que 0: '))
fatorial = num
operacao = num - 1
while operacao != 1:
    fatorial = operacao * fatorial
    operacao -= 1
print('{}! = {}'.format(num, fatorial))