print('===Orçamento - Pintura de Parede===')
l=float(input('Qual a largura, em metros, da parede a ser pintada?'))
h=float(input('Qual a altura, em metros, da parede a ser pintada?'))
a=l*h
t=a/2
print('A área da parede a ser pintada é de {:.2f}m².'.format(a))
print('A quantidade necessária de tinta para pintar uma parede de {:.2f} m² é de {:.2f} litros.'.format(a,t))
