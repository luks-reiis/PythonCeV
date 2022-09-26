print('='*40)
print('{:^40}'.format('Verificador de Gênero Sexual'))
print('='*40)
from time import sleep
print('''Qual seu gênero sexual?
Selecione:
[M] para Masculino
[F] para Feminino

''')
gensexo = str(input('Sua opção é: ')).strip().upper()
while gensexo != 'M' and gensexo != 'F':
    print('Opção inválida!!!')
    sleep(1)
    print('-'*40)
    print('Vamos tentar novamente!')
    print('''Qual seu gênero sexual?
    	Selecione:
     [M] para Masculino
     [F] para Feminino
     
     ''')
    gensexo = str(input('Sua opção é: ')).strip().upper()

