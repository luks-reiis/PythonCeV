from titulo import titulo
from linha import linha


def ficha(nome='<desconhecido>', gols=0):
    """
    ---> Função que irá mostrar a informação de um jogador em um campeonato.
    :param nome: (Opcional) Nome do jogador.
    :param gols: (Opcional) Quantidade de gols feito pelo jogador.
    :return: False
    """
    print(f'O jogador {nome}, fez {gols} gol(s) no campeonato.')


titulo('Função de Ficha do Jogador')
jogador = str(input('Nome do Jogador: '))
gol = str(input('Quantidade de gol(s): '))
linha()
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)
