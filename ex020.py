print('===Sortear uma ordem na lista===')
import random
a1 = input('Aluno 1:')
a2 = input('Aluno 2:')
a3 = input('Aluno 3:')
a4 = input('Aluno 4:')
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('Ordem de apresentação do trabalho: {}.'.format(lista))