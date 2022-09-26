print('===Primeiro e Último nome===')
nomec = str(input('Informe seu nome completo: ')).strip()
prim = nomec[:nomec.find(' ')]
ult = nomec[nomec.rfind(' ')+1:len(nomec)+1]
print('Primeiro nome: {}.'.format(prim))
print('Último nome: {}.'.format(ult))