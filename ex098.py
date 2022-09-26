from titulo import titulo
from linha import linha


def contador(i, f, p):
    from time import sleep
    if p == 0:
        p = 1
    if i <= f:
        for c in range(i, f + 1, p):
            print(c, end=' --> ', flush=True)
            sleep(0.5)
        print('FIM')
    elif i > f and p > 0:
        for c in range(i, f - 1, -p):
            print(c, end=' --> ', flush=True)
            sleep(0.5)
        print('FIM')
    elif i > f and p < 0:
        for c in range(i, f - 1, p):
            print(c, end=' --> ', flush=True)
            sleep(0.5)
        print('FIM')


titulo('Contador com Função')
print('Contagem de 1 até 10 de 1 em 1:')
contador(1, 10, 1)
linha()
print('Contagem de 10 até 0 de 2 em 2:')
contador(10, 0, -2)
linha()
print('Agora é com você! Defina os parâmetros do contador: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
linha()
