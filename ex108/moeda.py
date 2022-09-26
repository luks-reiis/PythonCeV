def dobro(v=0):
    return 2 * v


def metade(v=0):
    return v / 2


def aumentar(v=0, porc=0):
    final = v * (1 + porc / 100)
    return final


def diminuir(v=0, porc=0):
    final = v * (1 - porc / 100)
    return final


def moeda(v=0, cifra='R$'):
    return f'{cifra}{v:.2f}'.replace('.', ',')
