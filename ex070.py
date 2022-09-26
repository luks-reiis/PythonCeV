print('—'*40)
print('{:^40}'.format('Lojinha do Lucão'))
print('—'*40)
total = prod1000 = qtd = precobarato = 0
barato = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input(f'Preço de {produto}: R$'))
    continuar = ' '
    total += preco
    if preco > 1000:
        prod1000 += 1
    qtd += 1
    if qtd == 1:
        barato = produto
        precobarato = preco
    if precobarato > preco:
        precobarato = preco
        barato = produto
    while continuar not in 'SN':
        continuar = str(input ('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('—'*40)
print(f'a) Foram comprados {qtd} itens e o total foi de R${total}.')
print(f'b) {prod1000} produtos custam mais de R$1000.00.')
print(f'c) {barato} é o produto mais barato, custando R${precobarato}.')
