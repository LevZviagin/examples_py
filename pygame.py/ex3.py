import pygame
pygame.init

sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Класc Rect")
pygame.display.set_icon(pygame.image.load("app.bmp"))


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (32, 232, 106)  
ORANGE = (255, 158, 3)
BLACK = (0, 0, 0)
BRAUN = (87, 54, 19)
OXPA = (245, 161, 66)
GOLO = (66, 135, 245)

Size = 600
Size2 = 400

FPS = 100
clock = pygame.time.Clock()

ground = Size2-70
jump_force = 20
move = jump_force+1

hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(centerx=Size//2)
rect.bottom = ground
#print(rect)



while True:
    sc.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground == rect.bottom:
                move = -jump_force
                
    if move<=jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move+=1
                
        else:
            rect.bottom = ground
            move = jump_force+1
            
    sc.fill(WHITE)
    sc.blit(hero, rect)
    pygame.display.update()
    clock.tick(FPS)
            