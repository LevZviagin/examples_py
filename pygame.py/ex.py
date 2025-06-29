import pygame
pygame.init

sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Графичиские примитивы")
pygame.display.set_icon(pygame.image.load("app.bmp"))


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (32, 232, 106)
ORANGE = (255, 158, 3)
BLACK = (0, 0, 0)
BRAUN = (87, 54, 19)

Size = 600, 400

FPS = 60
clock = pygame.time.Clock()

pygame.draw.rect(sc, (0,255,0), (10,10, 50, 100))
pygame.draw.rect(sc, (255,0,0), (100,100, 100, 100))
pygame.display.update()

sp = None

sc.fill(WHITE)
pygame.display.update()

#flSartDraw = False #для рисования
#sp = ep = None

#sc.fill(WHITE)
#pygame.display.update()

pygame.mouse.set_visible(False)      #-(спрятать курсор мыши)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    sc.fill(WHITE)
    
    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_focused():
        pygame.draw.circle(sc, BLACK, pos, 7)
            
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        if sp is None:
            sp = pos
            
        width = pos[0] - sp[0]
        height = pos[1] - sp[1]
            
        sc.fill(WHITE)
        pygame.draw.rect(sc,GREEN,(sp[0], sp[1], width, height))
    else:
        sp = None
        
    pygame.display.update()
        #elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #flSartDraw = True
            #sp = event.pos
        #elif event.type == pygame.MOUSEMOTION:
            #if flSartDraw:
                #pos = event.pos               #-для рисования
                
                #width = pos[0] - sp[0]
                #height = pos[1] - sp[1]
                
                #sc.fill(WHITE)
                #pygame.draw.rect(sc,BRAUN, pygame.Rect(sp[0], sp[1], width, height))
                #pygame.display.update()
        #elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            #flSartDraw = False
#<_>
        #elif event.type == pygame.MOUSEBUTTONDOWN:
            #print("Нажата кнопка:", event.button)
        #elif event.type == pygame.MOUSEMOTION:          #-не для рисования
            #print("Позиция мыши:", event.rel)
            
    clock.tick(FPS)        
            