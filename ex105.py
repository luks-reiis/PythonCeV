from titulo import titulo


def notas(*n, sit = False):
    sala = {}
    maior = menor = soma = 0
    sala['total'] = len(n)
    for c in range(0, len(n)):
        soma += n[c]
        if c == 0:
            maior = menor = n[c]
        else:
            if n[c] > maior:
                maior = n[c]
            if n[c] < menor:
                menor = n[c]
    sala['maior'] = maior
    sala['menor'] = menor
    sala['média'] = soma / len (n)
    if sit:
        if sala['média'] < 6:
            situação = 'RUIM'
        if 6 <= sala['média'] < 7:
            situação = 'RAZOÁVEL'
        if 7 <= sala['média']:
            situação = 'BOA'
        sala['situação'] = situação                               
    return(sala)


#Programa Principal
titulo('Função de Analisar e Gerar Dicionários')
analise = notas(4.0, 5.0, 10, 1, 10, 10, 10, 10, sit = True)
print(analise)