print('===Ano Bissexto===')
ano = int(input('Informe um ano e eu direi se ele é bissexto: '))
if ano %400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    if ano %4 == 0:
        print('O ano {} é bissexto!'.format(ano))
    else:
        print('O ano {} não é bissexto!'.format(ano))
