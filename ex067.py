print('='*40)
print('{:^40}'.format('Tabuada com While / Break'))
print('='*40)
while True:
    num = int(input('A tabuada será de qual valor? '))
    cont = produto = 0
    print('*'*40)
    if num < 0:
        break
    cont += 1
    while cont < 11:
        produto = num * cont
        print(f'{num} X {cont} = {produto}')
        cont += 1
    print('*'*40)
print('Programa encerrado! Volte sempre!')
    

