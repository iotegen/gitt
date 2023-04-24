import pygame
clock=pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((618,359))#flags=pygame.NOFRAME
pygame.display.set_caption("BUku")
icon=pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)


bg=pygame.image.load('images/bg1.png')

walk_left = [
    pygame.image.load('images/p1.png'),
    pygame.image.load('images/p2.png'),
    pygame.image.load('images/p3.png'),
    pygame.image.load('images/p4.png'),
]

walk_right= [
    pygame.image.load('images/p5.png'),
    pygame.image.load('images/p6.png'),
    pygame.image.load('images/p7.png'),
    pygame.image.load('images/p8.png'),
]

player_anim_count=0
bg_x=0

while True:

    screen.blit(bg,(bg_x,0))
    screen.blit(bg,(bg_x+618,0))
    screen.blit(walk_right[player_anim_count],(300,250))
    


    if player_anim_count==3:
        player_anim_count=0
    else:    
        player_anim_count +=1

    bg_x-=2
    if bg_x==-618:
        bg_x=0    
    

    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(15)            
