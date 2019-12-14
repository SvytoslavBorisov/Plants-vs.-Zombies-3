import pygame
from classPlant import Plant, load_image


class Field:
    def __init__(self, width, height, cell_width, cell_height, left, top):
        self.width = width
        self.height = height
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.left = left
        self.top = top
        self.board = [[]]
        for i in range(self.width):
            for j in range(self.height):
                self.board[i].append('')
            self.board.append([])
        self.data = []

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                #pygame.draw.rect(screen, pygame.Color("white"),
                #                 pygame.Rect((self.left + j * self.cell_width,
                #                              self.top + i * self.cell_height),
                #                             (self.cell_width, self.cell_height)), 1)

                if self.board[j][i] != '':
                    self.board[j][i].update()
                    screen.blit(self.board[j][i].image, (self.cell_width * j + self.left,
                                               self.cell_height * i + self.top,
                                               self.cell_width,
                                               self.cell_height))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell):
        if self.board[cell[0]][cell[1]] == '':
            self.board[cell[0]][cell[1]] = Plant(plants['gatlingPea'])

    def get_cell(self, mouse_pos):
        self.data.clear()
        if self.left < mouse_pos[0] < self.left + self.width * self.cell_width \
                and self.top < mouse_pos[1] < self.top + self.height * self.cell_height:
            self.data.append((mouse_pos[0] - self.left) // self.cell_width)
            self.data.append((mouse_pos[1] - self.top) // self.cell_height)
            return self.data
        else:
            return None


pygame.init()
size = width, height = 700, 600
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen.fill((0, 0, 0))
GREEN = pygame.Color(0, 255, 0)
YELLOW = pygame.Color(0, 255, 255)
BLACK = pygame.Color(0, 0, 0)

plants = {'wallNut': [load_image(f'Graphics/animationGatlingPea/{i}.png', (80, 80)) for i in range(22)],
          'gatlingPea': [load_image(f'Graphics/animationGatlingPea/{i}.png', (80, 80)) for i in range(22)]}
sBackGround = pygame.image.load('Graphics/Frontyard.jpg').convert()
size = WIDTH, HEIGHT = 1026, 600

split_point_x = 1026
screen = pygame.display.set_mode(size)

screen.blit(sBackGround, (0, 0))
field = Field(9, 5, 82, 99, 245, 80)

running = True
while running:
    clock.tick(25)
    screen.fill(BLACK)
    screen.blit(sBackGround, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
           field.get_click(event.pos)

    field.render()
    pygame.display.flip()

pygame.quit()