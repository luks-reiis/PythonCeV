print('='*20)
print('Média de um aluno')
print('='*20)
nome = str(input('Nome do aluno: ')).strip().upper()
nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
media = (nota2 + nota1) / 2
print('A média do aluno {} é {:.1f}.'.format(nome, media))
if media < 5:
    print('{} está \033[0;31mREPROVADO\033[m!'.format(nome))
elif 5 <= media <= 6.9:
    print('{} está de \033[0;33mRECUPERAÇÃO\033[m!'.format(nome))
elif media >= 7.0:
    print('{} está \033[0;32mAPROVADO\033[m!'.format(nome))

