import random
print('='*20)
print('{:^20}'.format('JOKENPÔ'))
print('='*20)
nome = str(input('Digite seu nome:')).strip().upper()
print('Olá {}, será que você consegue me vencer em JOKENPÔ? \nJá te adianto que sou o melhor nesse jogo! XD'.format(nome))
print('''Então vamos lá, selecione uma das opções abaixo:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
sorte = random.randint(1,3)
opção = int(input('Sua opção é: '))
if opção == 1:
    if opção == sorte:
        print('Nós escolhemos PEDRA e empatamos! \nUfa, pelo menos não perdi, logo continuo sendo o melhor kkkkk')
    elif sorte == 2:
        print('Você escolheu PEDRA e eu escolhi PAPEL. \nBom, como sempre, eu ganhei kkkkk \nVocê não é páreo para o melhor jogador de JOKENPÔ!')
    else:
        print('Você escolheu PEDRA e eu escolhi TESOURA. \nEu perdi :( \nComo??? \nParabéns {}, você me venceu! Eu reconheço a minha derrota!'.format(nome))
elif opção == 2:
    if opção == sorte:
        print('Nós escolhemos PAPEL e empatamos! \nUfa, pelo menos não perdi, logo continuo sendo o melhor kkkkk')
    elif sorte == 3:
        print('Você escolheu PAPEL e eu escolhi TESOURA. \nBom, como sempre, eu ganhei kkkkk \nVocê não é páreo para o melhor jogador de JOKENPÔ!')
    else:
        print('Você escolheu PAPEL e eu escolhi PEDRA. \nEu perdi :( \nComo??? \nParabéns {}, você me venceu! Eu reconheço a minha derrota!'.format(nome))
elif opção == 3:
    if opção == sorte:
        print('Nós escolhemos TESOURA e empatamos! \nUfa, pelo menos não perdi, logo continuo sendo o melhor kkkkk')
    elif sorte == 1:
        print('Você escolheu TESOURA e eu escolhi PEDRA. \nBom, como sempre, eu ganhei kkkkk \nVocê não é páreo para o melhor jogador de JOKENPÔ!')
    else:
        print('Você escolheu PAPEL e eu escolhi PEDRA. \nEu perdi :( \nComo??? \nParabéns {}, você me venceu! Eu reconheço a minha derrota!'.format(nome))
else:
    print('{}, a opção que você escolheu é inválida! Tente novamente!'.format(nome))