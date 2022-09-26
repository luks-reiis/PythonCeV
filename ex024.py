print('===Validação Nome de Cidade Inicio da Lista===')
cidade = str(input('Informe o nome da cidade:')).strip()
nomescidade = cidade.split()
print('A cidade começa com "Santo"? {}'.format('santo'in nomescidade[0].lower()))
