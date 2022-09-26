print('='*40)
print(f'{"Valores Únicos em Uma Lista":^40}')
print('='*40)
i = 0
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    if valores[i] in valores[0:i]:
        valores.pop()
        print('Valor duplicado! Não será adicionado!')
    else:
        print('Valor adicionado com sucesso!')
    i = len(valores)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]'))[0].upper().strip()
    if resp in 'N':
        break
    
#Apenas a ordem de exibição da lista vai ser alterada:
print(f'Você digitou os valores {sorted(valores)}.')

#Para alterar a lista em ordem crescente:
#valores.sort()
#print(valores)
    
