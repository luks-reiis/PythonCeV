print('='*43)
print(f'{"Média Escolar com Dicionário Python":^43}')
print('='*43)
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    sit = 'aprovado'
elif 5 <= aluno['Média'] < 7:
    sit = 'recuperação'
else:
    sit = 'reprovado'
aluno['Situação'] = sit
print('='*43)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}.')
