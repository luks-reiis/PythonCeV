print('===Média das notas de um aluno===')
nome=input('Digite o nome do aluno:')
n1=float(input('Digite a primeira nota de {}:'.format(nome)))
n2=float(input('Digite a segunda nota de {}:'.format(nome)))
media=(n1+n2)/2
print('A média das notas de {} é {:.1f}.'.format(nome,media))
