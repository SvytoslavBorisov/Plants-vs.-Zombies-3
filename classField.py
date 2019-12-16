import pygame


class Field:
    def __init__(self, width, height, cell_width, cell_height, left, top, screen):
        self.width = width
        self.height = height
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.left = left
        self.top = top
        self.screen = screen
        self.board = [[]]
        for i in range(self.width):
            for j in range(self.height):
                self.board[i].append('')
            self.board.append([])
        self.data = []

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                """
                pygame.draw.rect(screen, pygame.Color("white"),
                                 pygame.Rect((self.left + j * self.cell_width,
                                              self.top + i * self.cell_height),
                                             (self.cell_width, self.cell_height)), 1)
                """
                if self.board[j][i] != '':
                    self.board[j][i].update()
                    self.screen.blit(self.board[j][i].image, (self.cell_width * j + self.left,
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
