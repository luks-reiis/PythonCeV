print('='*40)
print('{:^40}'.format('Menu de Opções'))
print('='*40)
from time import sleep
nome = str(input('Por favor informe seu nome: ')).strip().title()
print('Olá {}, no programa de hoje iremos manipular algumas propriedades de dois números. Então para isso:'.format(nome))
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
soma = 0
produto = 0
maior = num1
print('{}, escolha no menu abaixo o que deseja: '.format(nome))
print('''Menu:
[1] Somar os dois números
[2] Multiplicar os dois números
[3] Comparar os dois números
[4] Inserir novos números
[5] Finalizar o programa''')
menu = int(input('Sua opção é: '))
while menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5:
    print('Opção inválida, selecione novamente!')
    sleep(1)
    print('''Menu:
    [1] Somar os dois números
    [2] Multiplicar os dois números
    [3] Comparar os dois números
    [4] Inserir novos números
    [5] Finalizar o programa''')
    menu = int(input('Sua opção é: '))
while menu != 5:
    while menu == 1:
        soma = num1 + num2
        print('A soma dos números informados é igual a {}.'.format(soma))
        sleep(2)
        print('='*40)
        print('O que deseja fazer agora? ')
        print('''Menu:
        [1] Somar os dois números
        [2] Multiplicar os dois números
        [3] Comparar os dois números
        [4] Inserir novos números
        [5] Finalizar o programa''')
        menu = int(input('Sua opção é: '))
    while menu == 2:
        produto = num2 * num1
        print('A multiplicação dos números informados é igual a {}.'.format(produto))
        sleep(2)
        print('='*40)
        print('O que deseja fazer agora? ')
        print('''Menu:
        [1] Somar os dois números
        [2] Multiplicar os dois números
        [3] Comparar os dois números
        [4] Inserir novos números
        [5] Finalizar o programa''')
        menu = int(input('Sua opção é: '))
    while menu == 3:
        if num1 > num2:
            print('Dos números informados {} é o maior.'.format(num1))
        elif num2 > num1:
            print('Dos números informados {} é o maior.'.format(num2))
        elif num2 == num1:
            print('Os dois números são iguais.')
        sleep(2)
        print('='*40)
        print('O que deseja fazer agora? ')
        print('''Menu:
        [1] Somar os dois números
        [2] Multiplicar os dois números
        [3] Comparar os dois números
        [4] Inserir novos números
        [5] Finalizar o programa''')
        menu = int(input('Sua opção é: '))
    while menu == 4:
        num1 = float(input('Escolha um novo valor para o primeiro número: '))
        num2 = float(input('Escolha um novo valor para o segundo número: '))
        sleep(2)
        print('='*40)
        print('O que deseja fazer agora? ')
        print('''Menu:
        [1] Somar os dois números
        [2] Multiplicar os dois números
        [3] Comparar os dois números
        [4] Inserir novos números
        [5] Finalizar o programa''')
        menu = int(input('Sua opção é: '))
    while menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5:
        print('Opção inválida, selecione novamente!')
        sleep(1)
        print('''Menu:
        [1] Somar os dois números
        [2] Multiplicar os dois números
        [3] Comparar os dois números
        [4] Inserir novos números
        [5] Finalizar o programa''')
        menu = int(input('Sua opção é: '))
print('Tchau {}, volte quando quiser! :)'.format(nome))
