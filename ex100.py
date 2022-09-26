from titulo import titulo
from linha import linha
from time import sleep


def sorteia(lista):
    from random import randint
    for c in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Lista sorteada: {lista}.')
def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos pares da lista {lista} é igual a {soma}.')
def limpalista(lista):
    lista.clear()   
    

titulo('Funcões para Sortear e Somar')
numeros = []
while True:
    sorteia(numeros)
    somaPar(numeros)            
    linha()
    limpalista(numeros)
    sleep(5)            
            