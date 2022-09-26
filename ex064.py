print('='*40)
print('{:^40}'.format('Soma e Contagem de Vários Números'))
print('='*40)
print('*'*40)
print('{:^40}'.format('Flag = 999'))
print('*'*40)
num = 0
contagem = 0
soma = 0
while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        soma += num
        contagem += 1
print('Foram digitados {} números e a soma entre eles é igual a {}.'.format(contagem, soma))