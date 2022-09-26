def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;32mO usuário preferiu interromper o programa.\033[m')
            return 'para'
        else:
            return n


def linha(tam=43):
    return '=' * tam


def titulo(msg):
    print(linha())
    print(msg.center(43))
    print(linha())


def menu(lista):
    titulo('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'{cor("amarelo")}{cont}{cor("padrão")} - {cor("azul")}{item}{cor("padrão")}')
        cont += 1
    print(linha())
    escolha = leiaint(f'{cor("verde")}Sua opção:{cor("padrão")}')
    return escolha


def cor(escolha):
    cores = {'azul': '\033[0;34m',
             'vermelho': '\033[0;31m',
             'verde': '\033[0;32m',
             'padrão': '\033[m',
             'amarelo': '\033[0;33m'}
    return cores[f'{escolha}']


def leiaNome(msg):
    try:
        n = str(input(msg))
    except KeyboardInterrupt:
        print('\n\033[0;32mO usuário preferiu interromper o programa.\033[m')
    else:
        if n == '':
            n = '<desconhecido>'
        return n
