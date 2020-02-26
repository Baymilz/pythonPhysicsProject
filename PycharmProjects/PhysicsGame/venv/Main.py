import pygame
pygame.init()

winX = 500
winY = 500

win = pygame.display.set_mode((winX, winY))

pygame.display.set_caption("Newton's Laws")

x = 50
y = 50
width = 40
height = 40
vel = 5
str = 5

def redraw():
    win.fill((0,0,0))
    pygame.draw.rect(win, (0,0,255), (x, y, width, height))
    pygame.display.update()

run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    def checkMove():
        if keys[pygame.K_LEFT] and x > 0:
            x-=vel
        if keys[pygame.K_RIGHT] and x < winX:
            x+=vel
        if keys[pygame.K_UP] and y > 0:
            y-=vel
        if keys[pygame.K_DOWN] and y < winY:
            y+=vel

    checkMove()

    if keys[pygame.K_SPACE] and y > (str):
        for i in range(str):
            y-=str
            redraw()
            pygame.time.delay(75)
            checkMove()
        for i in range(str):
            y+=str
            redraw()
            pygame.time.delay(75)
            checkMove()

    redraw()

pygame.quit()
