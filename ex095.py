from time import sleep
print('='*82)
print(f'{"Cadastro de Jogador de Futebol V.2.0":^82}')
print('='*82)
time = []
jogador = {}
gols = []
selecionar = 0
while True:
    total = 0
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, part + 1):
        gols.append(int(input(f'Quantos gols na {c}ª partida? ')))
        total += gols[c - 1]
    jogador['gols'] = gols.copy()
    jogador['total'] = total
    time.append(jogador.copy())
    gols.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar mais jogadores? [S/N] '))[0].strip().upper()
    if resp == 'N':
        break
print('='*82)
print(f'{"Cod":<4}', end=' ')
print(f'{"Nome":<20}', end=' ')
print(f'{"Gols":>25}', end=' ')
print(f'{"Total":>30}')
print('—'*82)
for pos, j in enumerate(time):
    print(f'{pos + 1:<4}', end=' ')
    print(f'{j["nome"]:<20}', end=' ')
    print(f'{j["gols"]!s:>25}', end=' ')
    print(f'{j["total"]:>27}')
print('—'*82)
while True:
    selecionar = int(input('Mostrar dados de qual jogador? (Cod) '))
    while len(time) < selecionar or selecionar == 0:
        print('Erro! Não existe jogador para o código informado!')
        selecionar = int(input('Mostrar dados de qual jogador? (Cod) '))
    print(f'  Levantamento do jogador {time[selecionar - 1]["nome"]}:')
    for pos, v in enumerate(time[selecionar - 1]["gols"]):
        print(f'  No jogo {pos + 1} fez {v} gols.')
    print('—'*82)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Finalizar o Programa? [S/N]'))[0].strip().upper()
    if resp == 'S':
        break
print('—'*82)
print('Finalizando...')
sleep(1)
print(f'{"<<< Volte Sempre >>>":—^82}')
