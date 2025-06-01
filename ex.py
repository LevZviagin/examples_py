import pygame
pygame.init

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 158, 3)
BLACK = (0, 0, 0)
BRAUN = (87, 54, 19)

W, H = 600, 400
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Графичиские примитивы")
pygame.display.set_icon(pygame.image.load("app.bmp"))

FPS = 60
clock = pygame.time.Clock()

pygame.draw.rect(sc, (0,255,0), (10,10, 50, 100))
pygame.draw.rect(sc, (255,0,0), (100,100, 100, 100))
pygame.display.update()

flSartDraw = False
sp = ep = None

sc.fill(WHITE)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            flSartDraw = True
            sp = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if flSartDraw:
                pos = event.pos
                
                width = pos[0] - sp[0]
                height = pos[1] - sp[1]
                
                sc.fill(WHITE)
                pygame.draw.rect(sc,BRAUN, pygame.Rect(sp[0], sp[1], width, height))
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            flSartDraw = False
        #elif event.type == pygame.MOUSEBUTTONDOWN:
            #print("Нажата кнопка:", event.button)
        #elif event.type == pygame.MOUSEMOTION:
            #print("Позиция мыши:", event.rel)
            
    clock.tick(FPS)        
            