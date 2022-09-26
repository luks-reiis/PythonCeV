print('===Maior e Menor===')
num1 = int(input('Digite um número inteiro:'))
num2 = int(input('Digite outro número inteiro:'))
num3 = int(input('Digite o último número inteiro:'))
menor = num1
maior = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O maior número é {} e o menor {}.'.format(maior,menor))
