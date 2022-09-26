print('='*40)
print(f'{"Maior e Menor Valores na Lista":^40}')
print('='*40)
maior = menor = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um número inteiro para a posição {c}: ')))
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('='*40)
print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições', end=' ')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos}...', end='')
print()
