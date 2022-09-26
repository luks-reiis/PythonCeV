def titulo(msg):
    print('='*43)
    print(f'{msg:^43}')
    print('='*43)


def area(a, b):
    s = a * b
    print(f'A área de um terreno {a:.2f}m X {b:.2f}m é de {s:.2f}m².')


titulo('Função que cálcula área')
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
area(a, b)
