import pygame


class Field:
    def __init__(self, w, h, sw, sh, left, top):
        self.w, self.h, self.sw, self.sh, self.left, self.top =  w, h, sw, sh, left, top
        self.board = [[0] * self.w] * self.h
        
    def render(self):
        for i in range(self.h):
            for j in range(self.w):
                pygame.draw.rect(sc, pygame.Color("white"), pygame.Rect((self.left + j * self.sw, self.top + i * self.sh), (self.sw, self.sh)), 1)

    def clicked(self, i, j):
        self.board[i][j] = 1

    def count_cell(self, mx, my):
        kx = (mx - self.left) // self.sw
        ky = (my - self.top) // self.sh
        print(ky, kx)
        if 0 <= ky <= self.h - 1 and 0 <= kx <= self.w - 1: 
            self.clicked(ky, kx)
    
pygame.init()

size = width, height = 1026, 600
w, h, sw, sh, left, top = 9, 5, 83, 99, 241, 80
split_point_x = 1026
sc = pygame.display.set_mode(size)
BLACK = pygame.Color("black")

field = Field(w, h, sw, sh, left, top)

sBackGround = pygame.image.load('Graphics/Frontyard.jpg').convert()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            field.count_cell(*pygame.mouse.get_pos())
    
    sc.fill(BLACK)
    sc.blit(sBackGround, (0, 0))
    field.render()
    pygame.display.flip()

pygame.quit()
