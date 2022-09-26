def sistema():
    """
    ---> Programa automático de uma personalização do interactive help do Python.
    :return: False
    """
    from time import sleep
    cor = {'azul': '\033[0;30;44m',
           'vermelho': '\033[0;30;41m',
           'verde': '\033[0;30;42m',
           'padrão': '\033[m',
           'amarelo': '\033[0;30;43m'}
    while True:
        titulo = 'Sistema de Ajuda Personalizada'
        tamanho = len(titulo) + 2
        print(cor['verde'])
        print('='*tamanho)
        print(f' {titulo} ')
        print('='*tamanho)
        print()
        print(cor['padrão'])
        sel = str(input('Digite uma função ou biblioteca: ')).strip().lower()
        print()
        if sel == 'fim':
            print(cor['vermelho'])
            print('Finalizando o programa...')
            print()
            print(cor['padrão'])
            sleep(2)
            break
        print(cor['amarelo'])
        print(f"Acessando ajuda interativa de '{sel}'...")
        print()
        sleep(2)
        print(cor['azul'])
        help(sel)
        print()
        sleep(2)
        
        
sistema()
