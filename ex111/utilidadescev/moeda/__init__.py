def dobro(v=0, forma=False):
    if forma:
        return moeda(2 * v)
    else:
        return 2 * v


def metade(v=0, forma=False):
    if forma:
        return moeda(v / 2)
    else:
        return v / 2


def aumentar(v=0, porc=0, forma=False):
    final = v * (1 + porc / 100)
    if forma:
        return moeda(final)
    else:
        return final


def diminuir(v=0, porc=0, forma=True):
    final = v * (1 - porc / 100)
    if forma:
        return moeda(final)
    else:
        return final


def moeda(v=0.0, cifra='R$'):
    return f'{cifra}{v:.2f}'.replace('.', ',')


def resumo(v=0, sobe=0, reduz=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(v)}')
    print(f'Dobro do preço: \t{dobro(v, True)}')
    print(f'Metade do preço: \t{metade(v, True)}')
    print(f'{sobe}% de aumento: \t{aumentar(v, sobe, True)}')
    print(f'{reduz}% de redução: \t{diminuir(v, reduz, True)}')
    print('-'*30)