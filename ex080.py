print('='*40)
print(f'{"Lista Ordenada Sem Repetições":^40}')
print('='*40)
valores = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    # Poderia ser: if c == 0 or n > valores [len(valores)-1]
    if c == 0:
        valores.append(n)
        print(f'O valor {n} foi adicionado ao final da lista!')
    # Poderia ser: n > valores[-1]
    elif n > valores[len(valores)-1]:
        valores.append(n)
        print(f'O valor {n} foi adicionado ao final da lista!')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'O valor {n} foi adicionado na posição {pos}!')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {valores}.')
