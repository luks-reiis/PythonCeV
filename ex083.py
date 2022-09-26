print('='*40)
print(f'{"Analisando Expressões Matemáticas":^40}')
print('='*40)
pilha = []
exp = str(input('Digite uma expressão matemática: '))
for elementos in exp:
    if elementos == '(':
        pilha.append('(')
    elif elementos == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão matemática informada é válida!')
else:
    print('A expressão matemática informada está incorreta!')
