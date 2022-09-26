from titulo import titulo
from linha import linha


def fatorial(n, show=False):
    """
    ---> Função para calular o fatorial de um número.
    :param n: Número que será calculado o fatorial.
    :param show: (Opcional) Se 'True' mostrará o processo do cálculo do fatorial de 'n'.
    :return: Retorna o valor do fatorial de 'n'.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


help(fatorial)
titulo('Função que Calcula Fatorial')
while True:
    num = int(input('Digite um número inteiro: '))
    linha()
    resp = ' '
    while resp not in 'SN':
        resp = str(input(f'Deseja visualizar o processo de cálculo do fatorial de {num}? [S/N]'))[0].strip().upper()
        linha()
    if resp == 'S':
        print(fatorial(num, show=True))
    elif resp == 'N':
        print(f'O fatorial de {num} é {fatorial(num)}.')
    linha()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja calcular o fatorial de outro número? [S/N]'))[0].strip().upper()
        linha()
    if continuar == 'N':
        break
