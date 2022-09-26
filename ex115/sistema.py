from ex115.biblioteca.interface import *
from ex115.biblioteca.arquivo import *
from time import sleep

arq = 'dadoscadastrais.txt'
if arquivoExiste(arq):
    print(f'Arquivo {arq} encontrado com sucesso!')
else:
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas'.upper(), 'Cadastrar uma Nova Pessoa'.upper(), 'SAIR DO SISTEMA'])
    if resposta == 1:
        # Opção de ver as pessoas cadastradas
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        titulo('NOVO CADASTRO')
        nome = leiaNome('Nome: ')
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de finalizar o programa
        titulo(f'\t{cor("verde")}Finalizando o programa...{cor("padrão")}')
        sleep(2)
        print(f'{cor("verde")}VOLTE SEMPRE!!!{cor("padrão")}')
        break
    elif resposta == 'para':
        # Gambiarra kkkkkk
        break
    else:
        # Digitou uma opção errada no menu
        print(f'{cor("vermelho")}ERRO! Por favor escolha uma opção válida!{cor("padrão")}')
    sleep(2)
