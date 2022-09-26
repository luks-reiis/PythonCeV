from time import sleep
print('='*43)
print(f'{"Boletim com Listas Compostas":^43}')
print('='*43)
aluno = []
sala = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    sala.append(aluno[:])
    aluno.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] '))[0].strip().upper()
    if resp == 'N':
        break
print('='*43)
print(f'{"Nº":<4}', end='  ')
print(f'{"NOME":<30}', end='')
print(f'{"MÉDIA":>5}')
print('-'*43)
for pos, aluno in enumerate(sala):
    media = (aluno[1] + aluno[2]) / 2
    print(f'{pos + 1:<4}', end='  ')
    print(f'{aluno[0]:<30}', end='')
    print(f'{media:>5.1f}')
print('='*43)
while True:
    sel = int(input('Insira o Nº do aluno que deseja verificar as notas: '))
    if 0 < sel <= len(sala):
        print(f'Notas de {sala[sel-1][0]} são: {sala[sel-1][1:3]}')
    else:
        print('Não foi cadastrado aluno neste número!')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja verificar as notas de mais um aluno? [S/N] '))[0].strip().upper()
    if resp == 'N':
        break
    print('='*43)
print('='*43)
print('Finalizando...'.upper())
sleep(1)
print('<<< VOLTE SEMPRE >>>')
