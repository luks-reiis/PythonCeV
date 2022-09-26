print('='*20)
print('Cálculo IMC')
print('='*20)
nome = str(input('Qual seu nome? ')).strip().upper()
peso = float(input('{}, quanto você pesa em quilogramas? '.format(nome)))
altura = float(input('{}, qual a sua altura em metros? '.format(nome)))
imc = peso / altura ** 2
pesoideal = 24.9 * altura ** 2
print('{}, seu IMC é {:.1f}.'.format(nome, imc))
if imc < 18.5:
    print('{}, você está classificado em ABAIXO DO PESO!'.format(nome))
    print('Você deveria pesar no mínimo {:.1f}kg para estar classificado em PESO IDEAL!'.format(pesoideal))
elif 18.5 <= imc < 25:
    print('{}, você está classificado em PESO IDEAL!'.format(nome))
elif 25 <= imc < 30:
    print('{}, você está classificado em SOBREPESO!'.format(nome))
    print('Você deveria pesar no máximo {:.1f}kg para estar classificado em PESO IDEAL!'.format(pesoideal))
elif 30 <= imc < 40:
    print('{}, você está classificado em OBESIDADE!'.format(nome))
    print('Você deveria pesar no máximo {:.1f}kg para estar classificado em PESO IDEAL!'.format(pesoideal))
elif imc >= 40:
    print('{}, você está classificado em OBESIDADE MÓRBIDA!'.format(nome))
    print('Você deveria pesar no máximo {:.1f}kg para estar classificado em PESO IDEAL!'.format(pesoideal))
