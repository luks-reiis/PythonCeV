print('—'*40)
print(f'{"Análise de Dados com Listas Compostas":^40}')
print('—'*40)
pessoas = []
dados = []
pesado = leve = 0
while True:
    dados.append(str(input('Nome: ')).title())
    dados.append(float(input('Peso em kg: ')))
    if len(pessoas) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N] '))[0].strip().upper()
    if resp == 'N':
        break
print('—'*40)
print(f'A) Foram cadastradas {len(pessoas)} pessoas.')
print(f'B) O maior peso cadastrado foi de {pesado:.1f}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == pesado:
        print(f'[{p[0]}]', end='')
print()
print(f'C) O menor peso cadastrado foi de {leve:.1f}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == leve:
        print(f'[{p[0]}]', end='')
print()
