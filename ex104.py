from titulo import titulo
from linha import linha


def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('\033[0;31mErro! Por favor digite um número inteiro!\033[m')
            linha()


# Programa Principal
titulo('Função de verificação de número inteiro')
while True:
    num = leiaint('Digite um número inteiro: ')
    print(f'Você digitou o número {num}.')
    linha()
