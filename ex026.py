print('===Primeira e Última Ocorrência de uma String===')
frase = str(input('Escreva uma frase:'))
print('- Nesta frase existem {} letras "a".'.format(frase.count('a')))
print('- A primeira letra "a" desta frase encontra-se na posição: {}.'.format(frase.find('a')))