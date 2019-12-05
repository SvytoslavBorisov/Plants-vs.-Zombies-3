import pygame


pygame.init()
size = width, height = 700, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
GREEN = pygame.Color(0, 255, 0)
YELLOW = pygame.Color(0, 255, 255)
BLACK = pygame.Color(0, 0, 0)

sBackGround = pygame.image.load('Graphics/SelectorScreen_BG_Right.jpg').convert()

screen.blit(sBackGround, (0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()