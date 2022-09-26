print('=='*20)
print('Emprestimo para a compra de uma casa')
print('=='*20)
casa = float(input('Qual o valor em reais da casa? '))
sal = float(input('Qual o salário em reais do comprador? '))
tempo = int(input('Em quantos anos este empréstimo será pago? '))
mes = tempo*12
parcela = casa/mes
print('Parcelas de R${:.2f} por mês.'.format(parcela))
print('Valor percentual das parcelas em relação ao salário do comprador: {:.2f}%.'.format((parcela/sal)*100))
if parcela > 0.3*sal:
    print('O empréstimo para esse comprador foi negado!')
else:
    print('O empréstimo para esse comprador foi aprovado e a prestação será de R${:.2f} por mês durante um período de {} anos!'.format(parcela,tempo))