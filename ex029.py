print('\n===Limite de Velocidade===')
vel = int(input('\nVelocidade do carro em km/h: '))
multa = (vel - 80)*7
if vel > 80:
    print('\nVocê está sendo multado e precisará \npagar R${:.2f}!'.format(multa))
else:
    print('\nA sua velocidade está dentro dos limites \npermitidos, continue respeitando as leis detrânsito!')
    
