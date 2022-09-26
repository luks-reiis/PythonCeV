print('===Validação Dados em Uma Lista Independentemente da Posição na lista===')
nomecompleto = str(input('Informe seu nome completo:')).strip()
print('O nome {} possui "Silva"? {}'.format(nomecompleto.title(),'silva' in nomecompleto.lower()))