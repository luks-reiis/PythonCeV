print('===Aluguel de Carro===')
dia = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
custo = 0.15*km+60*dia
print('O total a ser pago é R${:.2f}.'.format(custo))