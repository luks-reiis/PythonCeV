print('===Triângulo V.1.0===')
lado1 = float(input('Digite o valor do primeiro segmento: '))
lado2 = float(input('Digite o valor do segundo segmento: '))
lado3 = float(input('Digite o valor do terceiro segmento: '))
if (abs(lado3 - lado2)) < lado1 < (lado3 + lado2) and (abs(lado3 - lado1)) < lado2 < (lado3 + lado1) and (abs(lado1 - lado2)) < lado3 < (lado1 + lado2):
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um trângulo!')