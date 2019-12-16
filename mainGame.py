import pygame
from classPlant import Plant, load_image, GatlingPea, Sunrise
import sys
FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = [""]

    fon = pygame.transform.scale(pygame.image.load('Graphics/other/fon.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


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
        global screen
        for i in range(self.height):
            for j in range(self.width):
                #pygame.draw.rect(screen, pygame.Color("white"),
                #                 pygame.Rect((self.left + j * self.cell_width,
                #                              self.top + i * self.cell_height),
                #                             (self.cell_width, self.cell_height)), 1)

                if self.board[j][i] != '':
                    temp = self.board[j][i].update()
                    if temp:
                        screen.blit(temp, (self.cell_width * j + self.left + 50,
                                               self.cell_height * i + self.top + 50,
                                               self.cell_width,
                                               self.cell_height))
                    screen.blit(self.board[j][i].image, (self.cell_width * j + self.left,
                                               self.cell_height * i + self.top,
                                               self.cell_width,
                                               self.cell_height))

    def get_click(self, mouse_pos, plant):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell, plant)

    def on_click(self, cell, plant):
        if self.board[cell[0]][cell[1]] == '':
            self.board[cell[0]][cell[1]] = plant

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

start_screen()

screen.fill((0, 0, 0))
GREEN = pygame.Color(0, 255, 0)
YELLOW = pygame.Color(0, 255, 255)
BLACK = pygame.Color(0, 0, 0)

plants = {'wallNut': [load_image(f'Graphics/animationGatlingPea/{i}.png', (80, 80)) for i in range(23)],
          'gatlingPea': [load_image(f'Graphics/animationGatlingPea/{i}.png', (80, 80)) for i in range(23)],
          'gatlingPeaShoot': [load_image(f'Graphics/animationGatlingPeaShoot/{i}.png', (80, 80)) for i in range(15)],
          'sunrise': [load_image(f'Graphics/animationSunrise/{i}.png', (80, 80)) for i in range(16)],
          'sunriseGiveSun': [load_image(f'Graphics/animationSunriseGiveSun/{i}.png', (80, 80)) for i in range(14)],
          'pea': load_image(f'Graphics/other/pea.png', (20, 20))}

sBackGround = pygame.image.load('Graphics/other/Frontyard.jpg').convert()
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
            if event.button == 1:
                field.get_click(event.pos, GatlingPea(plants['gatlingPea'], plants['gatlingPeaShoot'], plants['pea']))
            else:
                field.get_click(event.pos, Sunrise(plants['sunrise'], plants['sunriseGiveSun']))

    field.render()
    pygame.display.flip()

pygame.quit()