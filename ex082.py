print('='*40)
print(f'{"Dividindo valores em várias listas":^40}')
print('='*40)
todos = []
par = []
impar = []
while True:
    todos.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]'))[0].upper().strip()
    if resp in 'N':
        break
pos = 0
while pos < len(todos):
    if todos[pos] % 2 == 0:
        par.append(todos[pos])
    else:
        impar.append(todos[pos])
    pos += 1
print(f'A lista completa é {todos}.')
print(f'A lista dos pares é {par}.')
print(f'A lista dos ímpares é {impar}.')
