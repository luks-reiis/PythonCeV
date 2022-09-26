print('='*40)
print('{:^40}'.format('Análise de Dados do Grupo'))
print('='*40)
while True:
    nome = str(input('Nome da pessoa: '))
    idade = int(input(f'Idade de {nome}: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input(f'Qual o sexo de {nome}? [M/F] ')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break