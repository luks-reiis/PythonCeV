def leiaDinheiro(msg):
    while True:
        cont = 0
        digitado = str(input(msg)).replace(',', '.').strip()
        for c in digitado:
            if c == '.':
                cont += 1
        if digitado.isalpha() or digitado == '' or cont > 1 or digitado == '.':
            print(f'\033[0;31mERRO: "{digitado}" é um preço inválido!\033[m')
        else:
            digitado = float(digitado)
            return digitado
