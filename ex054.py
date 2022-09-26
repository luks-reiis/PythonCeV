print('='*30)
print('{:^30}'.format('Grupo da Maioridade'))
print('='*30)
from datetime import date
maiores = 0
for c in range (1,8):
    anos = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if (date.today().year - anos) >= 21:
        maiores += 1
menores = 7 - maiores
print('Dentre as pessoas citadas, existem {} maiores de idade e {} menores de idade'.format(maiores, menores))


