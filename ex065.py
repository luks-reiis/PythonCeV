print('='*40)
print('{:^40}'.format('Maior, Menor e Média com While'))
print('='*40)
contagem = 1
num = int(input('Digite um inteiro: '))
menor = maior = num
soma = num
resposta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
while resposta != 'S' and resposta != 'N':
    print('Opção inválida, tente novamente:')
    resposta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
while resposta == 'S':
    num = int(input('Digite um inteiro: '))
    contagem += 1
    soma += num
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    resposta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while resposta != 'S' and resposta != 'N':
        print('Opção inválida, tente novamente:')
        resposta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
media = soma / contagem
print('O MENOR valor digitado foi {}.'.format(menor))
print('O MAIOR valor digitado foi {}.'.format(maior))
print('A MÉDIA dos valores digitados é {:.2f}.'.format(media))