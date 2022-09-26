print('===Advinhe o Número===')
import random
print('Será que você consegue adivinhar, qual número estou pensando? XD')
num = int(input('Informe um número inteiro de 0 a 5: '))
sorte = random.randint(0,5)
if num == sorte:
    print('Parabéns o número {} era o que eu estava pensando! :).'.format(sorte))
else:
    print('Que pena você errou :(, o número que eu estava pensando era {}.'.format(sorte))

