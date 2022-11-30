import pygame
from random import randint
pygame.init()

x=950 # max 1250 min 520
y=470 # max 680 min 10
estrada_y = -1000
bot1_x=555
bot1_y=800 
bot2_x=790
bot2_y=100
bot3_x=1000
bot3_y=1000
bot4_x=1230
bot4_y=2000
velocidade=20
bot_velocidade=15
fundo = pygame.image.load('imagens/background.png')
estrada = pygame.image.load('imagens/road.png')
carro = pygame.image.load('imagens/mcqueen.png')
carro1 =  pygame.image.load('imagens/carro1.png')
carro2 =  pygame.image.load('imagens/carro2.png')
carro3 =  pygame.image.load('imagens/carro3.png')
carro4 =  pygame.image.load('imagens/carro4.png')

janela = pygame.display.set_mode((1900,950))
pygame.display.set_caption('Joguinho')

janela_aberta = True

while janela_aberta:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP] and y > 10:
        y-= velocidade
    if comandos[pygame.K_DOWN] and y < 680:
        y+= velocidade
    if comandos[pygame.K_RIGHT] and x < 1250:
        x+= velocidade
    if comandos[pygame.K_LEFT] and x > 520:
        x-= velocidade

    janela.blit(fundo,(0,0))
    janela.blit(estrada,(0,estrada_y))
    janela.blit(carro,(x,y))
    janela.blit(carro1,(bot1_x,bot1_y))
    janela.blit(carro2,(bot2_x,bot2_y))
    janela.blit(carro3,(bot3_x,bot3_y))
    janela.blit(carro4,(bot4_x,bot4_y))

    estrada_y += bot_velocidade
    if(estrada_y > -100):
        estrada_y = -1000

    bot1_y -= bot_velocidade
    if(bot1_y < -100):
        bot1_y = randint(1100,4000)
    
    bot2_y -= bot_velocidade
    if(bot2_y < -100):
        bot2_y = randint(1100,4000)
    
    bot3_y -= bot_velocidade
    if(bot3_y < -100):
        bot3_y = randint(1100,4000)
    
    bot4_y -= bot_velocidade
    if(bot4_y < -100):
        bot4_y = randint(1100,4000)


    pygame.display.update()

pygame.quit()