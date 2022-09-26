from datetime import date
print('='*25)
print('Classificação de atletas')
print('='*25)
nome = str(input('Digite o mome do atleta: ')).strip().upper()
nasc = int(input('Em que ano {} nasceu? '.format(nome)))
idade = date.today().year - nasc
if idade <= 9:
    print('{} tem {} anos e está classificado na categoria MIRIM.'.format(nome, idade))
elif 9 < idade <= 14:
    print('{} tem {} anos e está classificado na categoria INFANTIL.'.format(nome, idade))
elif 14 < idade <= 19:
    print('{} tem {} anos e está classificado na categoria JUNIOR.'.format(nome, idade))
elif 19 < idade <= 25:
    print('{} tem {} anos e está classificado na categoria SÊNIOR.'.format(nome, idade))
elif idade > 25:
    print('{} tem {} anos e está classificado na categoria MASTER.'.format(nome, idade))
