import pygame
from allConstants import *

class Panel:
    def __init__(self, height, cell_width, cell_height, left, top, step, screen):
        self.width = 1
        self.height = height
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.left = left
        self.top = top
        self.checkPlant = ''
        self.screen = screen
        self.step = step
        self.board = [[]]
        for i in range(self.width):
            for j in range(self.height):
                self.board[i].append('gatlingPea')
            self.board.append([])
        self.board[0][1] = 'sunrise'
        self.board[0][3] = 'wallNut'
        self.board[0][5] = 'sunrise'
        self.data = []

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                #pygame.draw.rect(self.screen, pygame.Color("white"),
                #                 pygame.Rect((self.left + j * self.cell_width,
                #                              self.top + i * self.cell_height + self.step * i),
                #                             (self.cell_width, self.cell_height)), 5)

                if self.board[j][i] != '':

                    self.screen.blit(cards[self.board[j][i]], (self.cell_width * j + self.left,
                                               self.cell_height * i + self.top + self.step * i,
                                               self.cell_width,
                                               self.cell_height))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell):
        self.checkPlant = self.board[cell[0]][cell[1]]

    def get_cell(self, mouse_pos):
        self.data.clear()
        if self.left < mouse_pos[0] < self.left + self.width * self.cell_width \
                and self.top < mouse_pos[1] < self.top + self.height * self.cell_height + self.step:
            self.data.append((mouse_pos[0] - self.left) // self.cell_width)
            self.data.append((mouse_pos[1] - self.top) // (self.cell_height + self.step))
            return self.data
        else:
            return None