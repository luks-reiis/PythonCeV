print('—'*40)
print('{:^40}'.format('Top 20 jogos de Mega Drive'))
print('—'*40)

#Classificação retirada do site: https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.ligadosgames.com/melhores-jogos-mega-drive/amp/&ved=2ahUKEwi_jrmJ9-X5AhWpr5UCHaJUB7gQFnoECA4QAQ&usg=AOvVaw07PeYSAWQXfETSFqh-pkrT

jogos = ('Sonic The Hedgehog 2','Golden Axe','Mortal Kombat',
         'Street Fighter II','Street of Rage 2','Rocket Knight Adventures',
         'Earthworm Jim',"Disney's Aladdin",'Altered Beast','Samurai Shodown',
         'Fifa 96','RoboCop vs Terminator','Comix Zone','Ristar','Castlevania: Bloodlines',
         'World of Illusion','X-Men 2: The Clone Wars',
         'TMNT: The Hyperstone Heist','Shining Force 2','Phantasy Star IV')
print('='*40)
print(f'Lista dos 20 melhores jogos do Mega Drive: {jogos}')
print('='*40)
print(f'Os 5 primeiros são: {jogos[0:5]}')
print('='*40)
print(f'Os 4 últimos são: {jogos[-4:]}')
print('='*40)
print(f'Jogos em ordem alfabética: {sorted(jogos)}')
print('='*40)
posicao = jogos.index('Altered Beast') + 1
print(f'O jogo Altered Beast está na {posicao}ª posição.')