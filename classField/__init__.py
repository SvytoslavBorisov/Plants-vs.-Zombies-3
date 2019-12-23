import pygame
from classPlant import *
from allConstants import *
from classPanel import *


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
        self.objects = []
        for i in range(self.width):
            for j in range(self.height):
                self.board[i].append('')
            self.board.append([])
        self.data = []

    def render(self):
        self.objects = []
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
                    if self.board[j][i].object:
                        for h in range(len(self.board[j][i].object)):
                            coord = self.board[j][i].object[h].update()
                            if coord:
                                self.objects.append([self.board[j][i].object[h], [self.board[j][i].object[h].image, coord], j, i, h])
        for x in self.objects:
            screen.blit(*x[1])

    def get_click(self, mouse_pos, checkPlant):
        cell = self.get_cell(mouse_pos)
        i = 0
        temp = []
        while i < len(self.objects):
            if self.objects[i][0].rect.collidepoint(mouse_pos):
                self.board[self.objects[i][2]][self.objects[i][3]].object[self.objects[i][4]].active = False
                del self.objects[i]
                print('+1 солнце')
            else:
                i += 1
        if cell and checkPlant:
            if self.on_click(cell, checkPlant):
                return True

    def on_click(self, cell, checkPlant):
        if self.board[cell[0]][cell[1]] == '':
            self.board[cell[0]][cell[1]] = choicePlant(checkPlant, [cell[0], cell[1]])
            return True

    def get_cell(self, mouse_pos):
        self.data.clear()
        if self.left < mouse_pos[0] < self.left + self.width * self.cell_width \
                and self.top < mouse_pos[1] < self.top + self.height * self.cell_height:
            self.data.append((mouse_pos[0] - self.left) // self.cell_width)
            self.data.append((mouse_pos[1] - self.top) // self.cell_height)
            return self.data
        else:
            return None
