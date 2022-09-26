print('===Reajuste Salarial Condicional===')
nome = str(input('Qual o nome do funcionário? '))
sal = float(input('Qual o salário em reais de {} atualmente? '.format(nome)))
if sal > 1250.00:
    print('O salário reajustado de {} será de R${:.2f}.'.format(nome, sal * 1.10))
else:
    print('O salário reajustado de {} será de R${:.2f}.'.format(nome, sal * 1.15))
