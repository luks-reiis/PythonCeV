print('='*43)
print(f'{"Unindo Dicionáros e Listas":^43}')
print('='*43)
grupo = []
pessoa = {}
somaidade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] '))[0].strip().upper()
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] '))[0].strip().upper()
    if resp == 'N':
        break
print(f'A) O grupo tem {len(grupo)} pessoas.')
for c in range(0, len(grupo)):
    somaidade += grupo[c]['idade']
media = somaidade / len(grupo)
print(f'B) A média da idade do grupo é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram:')
for c in range(0, len(grupo)):
    if grupo[c]['sexo'] == 'F':
        print(f'  => {grupo[c]["nome"]}')
print()
print('D) Pessoas com idade acima da média: ')
print()
for c in range(0, len(grupo)):
    if grupo[c]['idade'] > media:
        for k, v in grupo[c].items():
            print(f'{k} = {v}; ', end='')
        print()
print()
print('<< Análise Encerrada >>')
