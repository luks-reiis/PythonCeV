from ex107 import moeda
valor = float(input('Digite um valor: R$'))
print(f'O dobro de {valor} é {moeda.dobro(valor)}.')
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'Aumentando 10% do valor {valor}, o montante final será de {moeda.aumentar(valor, 10)}.')
print(f'Descontando 13% do valor {valor}, o montante final será de {moeda.diminuir(valor, 13)}.')
