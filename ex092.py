from datetime import date
print('='*43)
print(f'{"Cadastro de Trabalhador":^43}')
print('='*43)
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - nasc
resp = ' '
while resp not in 'SN':
    resp = str(input(f'{trabalhador["nome"]} possui carteira de trabalho? [S/N] '))[0].strip().upper()
if resp == 'S':
    trabalhador['ctps'] = int(input('Insira o nº da carteira de trabalho: '))
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = trabalhador['contratação'] + 35 - date.today().year + trabalhador['idade']
for k, v in trabalhador.items():
    print(f' - {k} tem o valor {v}.')
