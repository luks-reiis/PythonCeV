print('='*60)
print('{:^60}'.format('Listagem de Preços'))
print('='*60)
listagem = ('Manga Palmer (kg)',3.99,
         'Laranja Pera (kg)',2.49,
         'Goma de Tapioca Oishi',3.99,
         'Bolo Inglês',3.99,
         'Leite Integral Italac',4.89,
         'Leite Condensado Aurora',5.99,
         'Azeite Extra Virgem Carbonell',19.90,
         'Bombom Ferrero Rocher',24.90,
         'Amaciante Urca',10.98,
         'Hambúrguer Faroeste Aurora', 13.99,
         'Creme Dental Colgate',5.29,
         'Suco Integral Natural One (180ml)',2.19,
         'Café Cabloco',12.98,
         'Açúcar Refinado Da Barra',3.49,
         'Refrigerante Sprite',6.49)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<50}', end = '')
    else:
        print(f'R${listagem[pos]:>8.2f}')