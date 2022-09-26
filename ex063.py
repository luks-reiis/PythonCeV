print('='*40)
print('{:^40}'.format('Sequência de Fibonacci'))
print('='*40)
qtd = int(input('Digite a quantidade de elementos da sequência de Fibonacci que deseja ver: '))
p2 = 0
p1 = 1
pn = 0
termos = 1
print(0)
while termos < qtd:
    print(p1)
    pn = p1 + p2
    p2 = p1
    p1 = pn
    termos += 1
    

