print ('='*30)
print ('{:^30}'.format('Tabuada 2.0'))
print ('='*30)
num = int(input('Digite um número inteiro:'))
print (' ')
print ('Tabuada de {}:'.format(num))
print (' ')
for c in range(1,11):
    tabuada = num * c
    print('{} X {} = {}'.format(num, c, tabuada))