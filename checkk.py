import pygame
pygame.init()
screen=pygame.display.set_mode((900,600))#flags=pygame.NOFRAME
pygame.display.set_caption("BUku")
icon=pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

square=pygame.Surface((50,100))
square.fill("Red")

myfont=pygame.font.Font('fonts/static/Alkatra-SemiBold.ttf',40)
text_surface=myfont.render('tyagi',True,'Black')

player=pygame.image.load('images/icon.png')

while True:

    screen.fill((209, 135, 119))

    screen.blit(square,(10,0))
    screen.blit(text_surface,(75,50))
    screen.blit(player,(250,30))

    pygame.draw.circle(square,"Purple",(10,15),15)

    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
