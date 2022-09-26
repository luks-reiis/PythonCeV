from random import randint
from time import sleep
from operator import itemgetter
print('='*43)
print(f'{"Jogo de Dados":^43}')
print('='*43)
jogadores = {}
ranking = []
print(f'{"Valores sorteados:":^43}')
for c in range(1, 5):
    jogadores[f'jogador {c}'] = randint(1, 6)
    print(f'O jogador {c} tirou {jogadores[f"jogador {c}"]} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print()
print(f'{"<<< Ranking dos Jogadores >>>":=^43}')
for pos, v in enumerate(ranking):
    print(f"{f'{pos + 1}º lugar: {v[0]} com {v[1]} pontos.':^43}")
    sleep(1)
