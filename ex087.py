print('='*40)
print(f'{"Mais Sobre Matriz em Python":^40}')
print('='*40)
matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))
print('='*40)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna][0]:^4}]', end='')
    print()
print('='*40)
somapar = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna][0] % 2 == 0:
            somapar += matriz[linha][coluna][0]
