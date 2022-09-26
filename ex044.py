print('='*30)
print('Gerenciamento de Pagamentos')
print('='*30)
preco = float(input('Valor a ser pago: R$'))
print('''Selecione a forma de pagamento:
[1] À vista no dinheiro ou cheque;
[2] À vista no cartão;
[3] 2X no cartão;
[4] 3X ou mais no cartão.''')
opcao = int(input('Sua opção é:'))
if opcao == 1:
    print('Opção escolhida: Pagamento à vista no dinheiro ou cheque.')
    total = preco * 0.9
    print('O valor total a ser pago: R${:.2f}.'.format(total))
elif opcao == 2:
    print('Opção escolhida: Pagamento à vista no cartão.')
    total = preco * 0.95
    print('O valor total a ser pago: R${:.2f}.'.format(total))
elif opcao == 3:
    print('Opção escolhida: Pagamento em 2X no cartão.')
    total = preco
    parcelado = preco / 2
    print('Sua compra parcelada em 2X de R${:.2f} sem juros.'.format(parcelado))
    print('O valor total a ser pago: R${:.2f}.'.format(total))
elif opcao == 4:
    print('Opção escolhida: Pagamento em 3X ou mais no cartão.')
    parcelas = int(input('Em quantas parcelas você irá pagar? '))
    total = preco * 1.2
    parcelado = total / parcelas
    print('Sua compra parcelada em {}X de R${:.2f} com juros.'.format(parcelas, parcelado))
    print('O valor total a ser pago: R${:.2f}.'.format(total))
else:
    print('Opção inválida! Escolha novamente!')
