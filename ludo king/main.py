import pygame
import random

width = 1000
height = 900

#images
icon = pygame.image.load("assets\icon.png")
bg = pygame.image.load("assets/bg.png")

#squares
sq = pygame.image.load("assets\sq.png")
sr = pygame.image.load("assets/sr.png")
sb = pygame.image.load("assets/sb.png")
sy = pygame.image.load("assets/sy.png")
sg = pygame.image.load("assets/sg.png")
go_r = pygame.image.load("assets\gor.png")
go_b = pygame.image.load("assets\gob.png")
go_y = pygame.image.load("assets\goy.png")
go_g = pygame.image.load("assets\gog.png")
finnish = pygame.image.load("assets/finish.png")



win = pygame.display.set_mode((width, height))
pygame.display.set_caption("LUDO KING")
pygame.display.set_icon(icon)

#loop
run = True
while run:

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.blit(bg, (0,0))

    win.blit(sr, (100, 100))

    win.blit(sq, (200, 100))
    win.blit(sq, (300, 100))
    win.blit(go_r, (400, 100))
    win.blit(sq, (500, 100))
    win.blit(sq, (600, 100))
    win.blit(sg, (700, 100))

    win.blit(sq, (100, 200))
    win.blit(sq, (100, 300))
    win.blit(go_b, (100, 400))
    win.blit(sq, (100, 500))
    win.blit(sq, (100, 600))
    win.blit(sb, (100, 700))

    win.blit(sq, (700, 200))
    win.blit(sq, (700, 300))
    win.blit(go_g, (700, 400))
    win.blit(sq, (700, 500))
    win.blit(sq, (700, 600))
    win.blit(sy, (700, 700))
    
    win.blit(sq, (200, 700))
    win.blit(sq, (300, 700))
    win.blit(go_y, (400, 700))
    win.blit(sq, (500, 700))
    win.blit(sq, (600, 700))

    win.blit(sq, (400, 200))
    win.blit(sq, (400, 300))
    win.blit(finnish, (400, 400))
    win.blit(sq, (400, 500))
    win.blit(sq, (400, 600))

    win.blit(sq, (200, 400))
    win.blit(sq, (300, 400))
    win.blit(sq, (500, 400))
    win.blit(sq, (600, 400))


    pygame.display.update()