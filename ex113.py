def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print('\033[0;31mErro! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;32mO usuário preferiu interromper o programa.\033[m')
            break
        else:
            print(f'O número digitado foi {n}.')
            break


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except(TypeError, ValueError):
            print('\033[0;31mErro! Digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;32mO usuário preferiu interromper o programa.\033[m')
            break
        else:
            print(f'O número digitado foi {n}.')
            break
