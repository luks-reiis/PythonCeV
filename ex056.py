print('='*30)
print('{:^30}'.format('Analise de dados pessoais'))
print('='*30)
counthomem = 0
countmulher = 0
somaidade = 0
velho = 0
menosvinte = 0
nomevelho = ' '
for c in range (1,5):
    nome = str(input('Nome da {}ª pessoa: '.format(c))).strip().upper()
    idade = int(input('Idade de {}:'.format(nome)))
    print('Qual o sexo de {}?'.format(nome))
    print('''Escolha:
[1] Masculino
[2] Feminino ''')
    sexo = int(input('Sua opção: '))
    if sexo > 2:
        print('Opção inválida!!!Reinicie o Programa!!!')
    else:
        somaidade += idade
        if sexo == 1:
            counthomem += 1
            if idade > velho:
                velho = idade
                nomevelho = nome
        else:
            if idade < 20:
                menosvinte += 1
                countmulher += 1
    print('-'*40)
media = somaidade / 4
print('A média das idades das pessoas citadas é de {:.0f} anos.'.format(media))
if counthomem > 0:
    print('\nO nome do homem mais velho é {} com {} anos.'.format(nomevelho, velho))
if countmulher > 0:
    if countmulher > 1:
        print('\nDas pessoas que foram citadas, {} são mulheres com menos de 20 anos.'.format(menosvinte))
    if countmulher == 1:
        print('\nDas pessoas que foram citadas, {} é mulher com menos de 20 anos.'.format(menosvinte))

            
        