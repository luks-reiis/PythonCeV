from random import randint
from time import sleep
print('='*43)
print(f'{"Gerador de Jogos da Mega Sena":^43}')
print('='*43)
repetido = 0
duplicado = []
varios = []
jogo = []
qtd = int(input('Quantos jogos serão gerados? '))
for j in range(0, qtd):
    for c in range(0, 6):
        n = randint(1, 60)
        if c == 0:
            jogo.append(n)
        else:
            while n in jogo:
                n = randint(1, 60)
            jogo.append(n)
    jogo.sort()
    if jogo in varios:
        repetido += 1
        duplicado.append(jogo[:])
    varios.append(jogo[:])
    jogo.clear()
print()
print(f'{f" Gerando {qtd} jogos ":=^43}')
print()
for pos, j in enumerate(varios):
    print(f'Jogo {pos+1}: {j}')
    sleep(1)
print()
print(f'{" < BOA SORTE! > ":=^43}')
print(f'{repetido} jogos repetidos.')
print('Jogos repetidos:')
for j in duplicado:
    print(j)
