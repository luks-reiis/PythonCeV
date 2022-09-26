from ex109 import moeda
valor = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, forma=True)}.')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, forma=True)}')
print(f'Aumentando 10% do valor {moeda.moeda(valor)}, o montante final será de '
      f'{moeda.aumentar(valor, 10, forma=True)}.')
print(f'Descontando 13% do valor {moeda.moeda(valor)}, o montante final será de '
      f'{moeda.diminuir(valor, 13, forma=True)}.')
