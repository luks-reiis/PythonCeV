print ('='*40)
print ('{:^40}'.format('Soma dos impares multiplos de 3'))
print ('='*40)
s = 0
cont = 0
for c in range(1,501,1):
    if c %3 == 0 and c %2 != 0:
        s += c
        cont += 1
print ('''A soma dos {} números contidos num 
intervalo de 1-500 e atendem a condição de serem múltiplos de 3 e ímpares é: {}.'''.format(cont, s))
 

