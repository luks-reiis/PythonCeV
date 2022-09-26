from titulo import titulo
from linha import linha


def voto(ano):
    """""
    ---> Função que determina se uma pessoa possui voto obrigatório, opcional ou negado.
    :param ano: Ano de nascimento de uma pessoa.
    :return: False.
    """
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        print(f'Uma pessoa com {idade} anos NÃO VOTA!')
    elif 16 <= idade < 18 or idade >= 70:
        print(f'Com {idade} anos, o VOTO É OPCIONAL!')
    else:
        print(f'Com {idade} anos, o VOTO É OBRIGATÓRIO!')


titulo('Função para Votação')
nasc = int(input('Digite seu ano de nascimento: '))
linha()
voto(nasc)
