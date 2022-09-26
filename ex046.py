print('='*40)
print('{:^40}'.format('Contagem Regressiva'))
print('='*40)
import emoji
import time
for c in range(10,-1,-1):
    print(c)
    time.sleep(1)
print(emoji.emojize(":fireworks:"*10, language='alias'))
