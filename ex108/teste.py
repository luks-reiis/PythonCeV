from ex108 import moeda
valor = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}.')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'Aumentando 10% do valor {moeda.moeda(valor)}, o montante final será de '
      f'{moeda.moeda(moeda.aumentar(valor, 10))}.')
print(f'Descontando 13% do valor {moeda.moeda(valor)}, o montante final será de '
      f'{moeda.moeda(moeda.diminuir(valor, 13))}.')
