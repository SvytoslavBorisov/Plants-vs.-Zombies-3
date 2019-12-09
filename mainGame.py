import pygame
from classPlant import Plant


pygame.init()
size = width, height = 1366, 768
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill((0, 0, 0))
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
plants = Plant('Wallnut_body', (80, 80))
backGame = pygame.transform.scale(pygame.image.load('Graphics/backGame.png'), (width, height))
Card_GatlingPea = pygame.transform.scale(pygame.image.load('Graphics/Card_GatlingPea.png'), (100, 100))
screen.blit(backGame, (0, 0))


class BoardOfCards:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [['yellow'] * height for _ in range(width)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.data = []

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for g in range(self.width):
            for i in range(self.height):
                pygame.draw.rect(screen, WHITE, (g * self.cell_size + self.left,
                                                 i * self.cell_size + self.top, self.cell_size,
                                                 self.cell_size))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell):
        if cell:
            screen.blit(Card_GatlingPea, (self.cell_size * cell[0] + self.left,
                                          self.cell_size * cell[1] + self.top,
                                          self.cell_size,
                                          self.cell_size))

    def get_cell(self, mouse_pos):
        self.data.clear()
        if self.left < mouse_pos[0] < self.left + self.width * self.cell_size \
                and self.top < mouse_pos[1] < self.top + self.height * self.cell_size:
            self.data.append((mouse_pos[0] - self.left) // self.cell_size)
            self.data.append((mouse_pos[1] - self.top) // self.cell_size)
            return self.data
        else:
            return None


class BoardOfGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [['green'] * height for _ in range(width)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.data = []

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for g in range(self.width):
            for i in range(self.height):
                pygame.draw.rect(screen, WHITE, (g * self.cell_size + self.left,
                                                 i * self.cell_size + self.top,
                                                 self.cell_size,
                                                 self.cell_size), 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell):
        screen.blit(plants.image, (self.cell_size * cell[0] + self.left,
                                   self.cell_size * cell[1] + self.top,
                                   self.cell_size,
                                   self.cell_size))

    def get_cell(self, mouse_pos):
        self.data.clear()
        if self.left < mouse_pos[0] < self.left + self.width * self.cell_size \
                and self.top < mouse_pos[1] < self.top + self.height * self.cell_size:
            self.data.append((mouse_pos[0] - self.left) // self.cell_size)
            self.data.append((mouse_pos[1] - self.top) // self.cell_size)
            return self.data
        else:
            return None


boardGame = BoardOfGame(9, 5)
boardGame.set_view(240, 104, 80)
boardGame.render()

boardCards = BoardOfCards(1, 5)
boardCards.set_view(5, 5, 100)
boardCards.render()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            boardCards.get_click(event.pos)
            boardGame.get_click(event.pos)

    pygame.display.flip()

pygame.quit()