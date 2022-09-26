import math
print('===Catetos e Hipotenusa===')
catop = float(input('Insira o valor do cateto oposto de um triângulo retângulo:'))
catad = float(input('Insira o valor do cateto adjacente de um triângulo retângulo:'))
hipot = math.hypot(catop,catad)
print('O valor da hipotenusa deste triângulo retângulo é {}.'.format(hipot))
      