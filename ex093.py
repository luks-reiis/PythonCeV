print('='*43)
print(f'{"Cadastro de Jogador de Futebol":^43}')
print('='*43)
jogador = {}
gols = []
total = 0
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, part + 1):
    gols.append(int(input(f'Quantos gols na {c}ª partida? ')))
    total += gols[c - 1]
jogador['gols'] = gols.copy()
jogador['total'] = total
print('='*43)
print(jogador)
print('='*43)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('='*43)
print(f'O jogador {jogador["nome"]} jogou {part} paridas.')
for pos, v in enumerate(gols):
    if v == 1:
        print(f' - Na {pos + 1}ª partida, fez {v} gol.')
    else:
        print(f' - Na {pos + 1}ª partida, fez {v} gols.')
print(f'Foi um total de {total} gols.')
