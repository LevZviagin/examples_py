import pygame
pygame.init

sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Класс Surface")
pygame.display.set_icon(pygame.image.load("app.bmp"))


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (32, 232, 106)  
ORANGE = (255, 158, 3)
BLACK = (0, 0, 0)
BRAUN = (87, 54, 19)

Size = 600
Size2 = 400

FPS = 100
clock = pygame.time.Clock()

sc.fill(WHITE)
pygame.display.update()

surf = pygame.Surface((Size, 200))
bita = pygame.Surface((50, 10))

surf.fill(BLUE)
bita.fill(GREEN)

bx = 0
by = 150
x = 0
y = 0

#pygame.draw.rect(sc, (0,255,0), (10,10, 50, 100))
#pygame.draw.rect(sc, (255,0,0), (100,100, 100, 100))
#pygame.display.update()

#sp = None


#sc.fill(WHITE)
#pygame.display.update()



#pygame.mouse.set_visible(False)      #-(спрятать курсор мыши)

while True:
    sc.fill(WHITE)
    
    #pos = pygame.mouse.get_pos()
    #if pygame.mouse.get_focused():
        #pygame.draw.circle(sc, GREEN, pos, 7)  
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    surf.fill(BLUE)
    surf.blit(bita, (bx, by))
    if bx < Size:
        bx += 5
    else:
        bx = 0
        
    if y < Size2:
        y += 1
    else:
        y = 0
    
    sc.fill(WHITE)
    sc.blit(surf, (x, y))        
    #sc.fill(WHITE)
    #pos = pygame.mouse.get_pos()
    #if pygame.mouse.get_focused():
        #pygame.draw.circle(sc, GREEN, pos, 7)

    pygame.display.update()  #-не использовать
        
    clock.tick(FPS)        
            