import pygame
clock=pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((618,359))#flags=pygame.NOFRAME
pygame.display.set_caption("BUku")
icon=pygame.image.load('proekt/images/icon.png').convert_alpha()
pygame.display.set_icon(icon)


bg=pygame.image.load('proekt/images/bg1.png').convert_alpha()

walk_left = [
    pygame.image.load('proekt/images/p1.png').convert_alpha(),
    pygame.image.load('proekt/images/p2.png').convert_alpha(),
    pygame.image.load('proekt/images/p3.png').convert_alpha(),
    pygame.image.load('proekt/images/p4.png').convert_alpha(),
]

walk_right= [
    pygame.image.load('proekt/images/p5.png').convert_alpha(),
    pygame.image.load('proekt/images/p6.png').convert_alpha(),
    pygame.image.load('proekt/images/p7.png').convert_alpha(),
    pygame.image.load('proekt/images/p8.png').convert_alpha(),
]

ghost=pygame.image.load('proekt/images/ghost.png').convert_alpha()
##ghost_x=620
ghost_list_in_game=[]

player_anim_count=0
bg_x=0

player_speed=5
player_x=150
player_y=250

is_jump=False
jump_count=9

bg_sound=pygame.mixer.Sound('proekt/the-weeknd-is-there-someone-else.mp3')
bg_sound.play()

ghost_timer=pygame.USEREVENT +1
pygame.time.set_timer(ghost_timer,2500)

label=pygame.font.Font('fonts/static/Alkatra-Bold.ttf',40)
lose_label = label.render('Tyagi lose!',False,(193,196,199))   
restart_label = label.render('Play again',False,(115,132,148))
restart_label_rect =restart_label.get_rect(topleft=(180,200))   

bullets_left = 5
bullet=pygame.image.load('proekt/images/bullet.png').convert_alpha()
bullets=[]
gameplay=True


while True:

    screen.blit(bg,(bg_x,0))
    screen.blit(bg,(bg_x+618,0))
    ##screen.blit(ghost,(ghost_x,230))

    if gameplay:

        player_rect = walk_left[0].get_rect(topleft=(player_x,player_y))
        ##ghost_rect=ghost.get_rect(topleft=(ghost_x,230))

        if ghost_list_in_game:
            for (i,el) in enumerate(ghost_list_in_game):
                screen.blit(ghost,el)
                el.x-=10

                if el.x <-10:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    # print("U lose!") 
                    gameplay=False

                # if player_rect.colliderect(ghost_rect):
                #      print("U lose!")


        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count],(player_x,player_y))
        else:
            screen.blit(walk_right[player_anim_count],(player_x,player_y))

        if keys[pygame.K_LEFT] and player_x>50:
            player_x-=player_speed
        elif keys[pygame.K_RIGHT] and player_x<550:
            player_x+=player_speed    

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump=True
        else:
            if jump_count >= -9:
                if jump_count > 0:
                    player_y -= (jump_count**2)/2
                else:
                    player_y += (jump_count**2)/2
                jump_count-=1                        
            else:
                is_jump=False
                jump_count=9

        if player_anim_count==3:
            player_anim_count=0
        else:    
            player_anim_count +=1

        bg_x-=2
        if bg_x==-618:
            bg_x=0    
        
        ##ghost_x-=10

        # if keys[pygame.K_b]:
        #     bullets.append(bullet.get_rect(topleft=(player_x+30,player_y+10)))

        if bullets:
            for (i,el) in enumerate(bullets):
                screen.blit(bullet,(el.x,el.y))
                el.x+=4

                if el.x>630:
                    bullets.pop(i)

                if ghost_list_in_game:
                    for(index,ghost_el) in enumerate(ghost_list_in_game):
                        if el.colliderect(ghost_el):
                            ghost_list_in_game.pop(index)
                            bullets.pop(i)

    else:
        screen.fill((87,88,89))
        screen.blit(lose_label,(180,100))
        screen.blit(restart_label,restart_label_rect)

        mouse=pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay=True
            player_x=150
            ghost_list_in_game.clear()
            bullets.clear()
            bullets_left=5

    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type==ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(620,250)))
        if gameplay and event.type == pygame.KEYUP and event.key==pygame.K_b and bullets_left>0:
            bullets.append(bullet.get_rect(topleft=(player_x+30,player_y+10))) 
            bullets_left -=1
    clock.tick(20)            
