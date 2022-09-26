print('='*40)
print('{:^40}'.format('Jogo par ou ímpar'))
print('='*40)
from random import randint
print('Vamos jogar par ou ímpar!')
count = 0
while True:
    sorte = randint(0,10)
    num = int(input('Digite um número inteiro: '))
    escolha = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    while escolha != 'P' and escolha != 'I':
        print('Opção inválida!')
        escolha = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    soma = num + sorte
    print (f'Você escolheu {num} e eu escolhi {sorte}. \nTotal de {soma}.')
    if soma %2 == 0:
        print('Deu par')
        if escolha == 'P':
            count += 1
            print ('Você ganhou...')
            print ('Vamos continuar!')
        else:
            print('Você perdeu kkkkk')
            break
    else:
        print ('Deu ímpar')
        if escolha == 'I':
            count += 1
            print ('Você ganhou...')
            print ('Vamos continuar!')
        else:
            print ('Você perdeu kkkkk')
            break
    print('*'*40)
print('*'*40)
print('Game Over :(')
print(f'Seu placar foi de {count} acertos.')

            