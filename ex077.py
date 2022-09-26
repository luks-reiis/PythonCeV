print('='*40)
print(f'{"Contando vogais em tuplas":^40}')
print('='*40)
palavras = ('Engenharia', 'Eletrica', 'Python','Preventiva','Relatorio','Cabine','Primaria',
            'Laudo', 'Ensaio', 'Comercial', 'Controlador', 'Proteçao', 'Sistema','Aprendizado',
            'Faculdade', 'Dinheiro', 'Estabilidade', 'Automaçao', 'Viver')
for p in palavras:
    print(f'Na palavra {p.upper()} temos as vogais: ', end='')
    for vogal in p:
        if vogal.upper() in 'AEIOU':
            print(vogal.upper(), end='  ')
    print('')