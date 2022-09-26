print('='*30)
print('Conversor de bases numéricas')
print('='*30)
num = int(input('Digite um número inteiro: '))
print('''Selecione uma base de conversão:
[1] para binário;
[2] para octal;
[3] para hexadecimal.''')
base = int(input('A base de conversão que você deseja é: '))
if base == 1:
    print('O número {} convertido em binário é {}.'.format(num, bin(num)[2:]))
elif base == 2:
    print('O número {} convertido em octal é {}.'.format(num, oct(num)[2:]))
elif base == 3:
    print('O número {} convertido em hexadecimal é {}.'.format(num, hex(num)[2:].upper()))
else:
    print('A opção escolhida é inválida, selecione novamente!')
