print('===Parte inteira de um número real===')
import math
num = float(input('Digite um número:'))
inteiro = math.trunc(num)
print('A parte inteira de {} é {}.'.format(num,inteiro))