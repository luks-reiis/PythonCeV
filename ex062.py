print('='*40)
print('{:^40}'.format('P.A. 3.0'))
print('='*40)
p1 = float(input('Digite o primeiro termo de uma PA: '))
r = float(input('Qual a razão dessa PA? '))
n = 1
pn = 0
resposta = 'S'
print('Os 10 primeiros termos dessa progressão aritmética são:')
while n < 11:
    pn = p1 + (n-1)*r
    print (pn)
    n += 1
t = n
t += int(input('Deseja adicionar mais quantos termos? '))
while t > n:
    pn = p1 + (n-1)*r
    print(pn)
    n += 1
    if n == t:
        t += int(input('Deseja adicionar mais quantos termos? '))
