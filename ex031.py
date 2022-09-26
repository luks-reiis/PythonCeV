print('\n ===Preço da Viagem===')
km = int(input('\n Qual a distância da viagem em km? '))
preco1 = km * 0.45
preco2 = km * 0.50
if km < 200:
    print('\n O total a ser pago pela viagem \nserá de R${:.2f}.'.format(preco1))
else:
    print('\n O total a ser pago pela viagem \nserá de R${:.2f}.'.format(preco2))