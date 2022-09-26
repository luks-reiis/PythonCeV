from datetime import date
print('='*20)
print('Alistamento Militar')
print('='*20)
nome = str(input('Qual seu nome? ')).strip().upper()
anos = int(input('{}, em que ano você nasceu? '.format(nome)))
atual = date.today().year
idade = atual - anos
print('Você tem {} anos, pois nasceu no ano de {}.'.format(idade, anos))
if idade > 18:
    saldo = idade - 18
    print('{}, você deveria ter se alistado há {} anos!'.format(nome, saldo))
    print('Seu alistamento foi em {}.'.format(anos + 18))
elif idade == 18:
    print('{}, você precisa se alistar neste ano imediatemente!'.format(nome))
elif idade < 18:
    saldo = 18 - idade
    print('{}, você precisará se alistar daqui a {} anos!'.format(nome, saldo))
    print('Seu alistamento será em {}.'.format(anos + 18))

