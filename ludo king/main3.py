import pygame
import random

width = 1000
height = 900

#images
icon = pygame.image.load("assets\icon.png")
bg = pygame.image.load("assets/bg.png")

#dice images
dice1 = pygame.image.load("assets/dice1.png")
dice2 = pygame.image.load("assets/dice2.png")
dice3 = pygame.image.load("assets/dice3.png")
dice4 = pygame.image.load("assets/dice4.png")
dice5 = pygame.image.load("assets/dice5.png")
dice6 = pygame.image.load("assets/dice6.png")

#rolling the dice
def roll(pos):
    pos = [1, 2, 3, 4, 5, 6]
    rolling = random.choices(pos)
    if rolling == [1]:
        win.blit(dice1, (0 , 0))
    if rolling == [2]:
        win.blit(dice2, (0 , 0))
    if rolling == [3]:
        win.blit(dice3, (0 , 0))
    if rolling == [4]:
        win.blit(dice4, (0 , 0))
    if rolling == [5]:
        win.blit(dice5, (0 , 0))
    if rolling == [6]:
        win.blit(dice6, (0 , 0))


#players
red = pygame.image.load("assets/r_player.png")
blue = pygame.image.load("assets/b_player.png")
yellow = pygame.image.load("assets/y_player.png")
green = pygame.image.load("assets/g_player.png")

#player rect

redrect = red.get_rect()
bluerect = blue.get_rect()
yellowrect = yellow.get_rect()
greenrect = green.get_rect()

#player position
redrect.topleft = 250, 250
bluerect.topleft = 250, 550
yellowrect.topleft = 550, 550
greenrect.topleft = 550, 250



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

#loop
run = True
while run:

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                roll(pos=[1, 2, 3, 4, 5, 6])


    #player
    win.blit(red, redrect)
    win.blit(green, greenrect)
    win.blit(yellow, yellowrect)
    win.blit(blue, bluerect)


    pygame.display.update()
