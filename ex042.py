print('='*20)
print('Triângulo V.2.0')
print('='*20)
lado1 = float(input('Digite o valor do primeiro segmento: '))
lado2 = float(input('Digite o valor do segundo segmento: '))
lado3 = float(input('Digite o valor do terceiro segmento: '))
if (abs(lado3 - lado2)) < lado1 < (lado3 + lado2) and (abs(lado3 - lado1)) < lado2 < (lado3 + lado1) and (abs(lado1 - lado2)) < lado3 < (lado1 + lado2):
    print('Os segmentos acima PODEM formar um triângulo!')
    if lado1 == lado2 and lado1 == lado3 and lado3 == lado2:
        print('O triângulo é EQUILÁTERO.')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('O triângulo é ESCALENO.')
    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print('O triângulo é ISÓSCELES.')
else:
    print('Os segmentos acima não PODEM formar um trângulo!')