print('='*30)
print('{:^30}'.format('Progressão Aritmética'))
print('='*30)
p1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
p10 = p1 + (10-1)*r
for c in range(p1, p10 + 1 , r):
    print (c)
