def escreva(msg):
    print('~'*(len(msg)+2))
    print(f' {msg} ')
    print('~' * (len(msg) + 2))


from titulo import titulo
from linha import linha
titulo('Print com Função')
escreva('Lucas')
escreva('Manutenção Preventiva')
escreva('Ensaio de Isolação')
escreva('Olá Mundo!!!')
formatar = str(input('Agora é com você! Digite uma frase: ')).strip()
escreva(formatar)
linha()