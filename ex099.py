from titulo import titulo
from random import randint
from linha import linha
from time import sleep


def maior(lista):
    m = 0
    for pos, e in enumerate(lista):
        if pos == 0 or e > m:
            m = e
    print(f'Dentre os valores {lista}, o maior é {m}')


titulo('Função que Descobre o Maior')
valores = []
for c in range(0, 6):
    for c in range(0, 3):
        valores.append(randint(0, 100))
    maior(valores)
    linha()
    valores.clear()
    sleep(2)
