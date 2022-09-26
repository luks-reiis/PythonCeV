print('='*30)
print('{:^30}'.format('Detector de Palíndromos'))
print('='*30)
frase = str(input('Digite uma frase: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letras in range (len(junto) - 1, -1, -1):
    inverso += junto[letras]
if inverso == junto:
    print('\nA frase {} e o seu inverso {} são palíndromos.'.format(junto, inverso))
else:
    print('\nA frase {} e o seu inverso {} não são palíndromos.'.format(junto, inverso))
