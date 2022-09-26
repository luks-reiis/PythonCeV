print('='*40)
print('{:^40}'.format('Advinhe o Número 2.0'))
print('='*40)
from time import sleep
import random
tentativas = 1
continuar = 'S'
while continuar == 'S':
    print('\nSerá que você consegue adivinhar, qual número estou pensando? XD')
    num = int(input('\nInforme um número inteiro de 0 a 10: '))
    sorte = random.randint(0,10)
    while num != sorte:
        print('\n- Som de Tambores Batendo...')
        sleep(2)
        print('\nPoxa vida, você não acertou. Mas não desista amigo, eu sei que você consegue ;)')
        sleep(1)
        if num > sorte:
            print('\n Vou te dar uma dica, ele é menor do que {} ;)'.format(num))
        elif num < sorte:
            print('\n Vou te dar uma dica, ele é maior do que {} ;)'.format(num))
        sleep(1)
        num = int(input('\nQual seu próximo palpite? '))
        tentativas += 1
    print('\n- Som de Tambores Batendo...')
    sleep(2)
    print('\nParabéns você conseguiu adivinhar o número que eu estava pensando! :)')
    sleep(1)
    print('\nVocê deu {} palpites para acertar o número que eu estava pensando.'.format(tentativas))
    if tentativas == 1:
        print('\nAmigo, você é um(a) vidente?')
    else:
        print('\nSerá que você consegue acertar meu número apenas com 1 palpite?')
    print('-'*40)
    sleep(2)
    continuar = str(input('\nDeseja jogar novamente? [S/N]')).upper().strip()

