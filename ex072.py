print('—'*40)
print('{:^40}'.format('Números por Extenso'))
print('—'*40)
escrito = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
num = int(input('Digite um número inteiro e que esteja entre 0 e 20: '))
while True:
    if num > 20 or num < 0:
        num = int(input('Tente novamente, digite um número inteiro e que esteja entre 0 e 20: '))
    else:
        break
print('—'*40)
print(f'Você digitou o número {escrito[num]}.')