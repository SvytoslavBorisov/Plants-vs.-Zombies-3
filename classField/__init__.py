import pygame
from classPlant import *
from allConstants import *
from classPanel import *


class Field:
    def __init__(self, width, height, cell_width, cell_height, left, top, screen, game):
        self.width = width
        self.height = height
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.left = left
        self.top = top
        self.screen = screen
        self.game = game
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
            self.screen.blit(plants['lownMower'], (self.left - 75,
                                               self.cell_height * i + self.top,
                                               self.cell_width,
                                               self.cell_height))
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
                    if self.board[j][i].objects:
                        for h in range(len(self.board[j][i].objects)):
                            coord = self.board[j][i].objects[h].update()
                            if coord:
                                self.objects.append([self.board[j][i].objects[h], [self.board[j][i].objects[h].image, coord], j, i, h])
        for x in self.objects:
            screen.blit(*x[1])

    def mouse_move(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            scr = pygame.Surface((FIELD_CELL_WIDTH, FIELD_CELL_HEIGHT * FIELD_HEIGHT))
            scr.set_alpha(128)
            scr.fill(pygame.Color(255, 255, 0))
            screen.blit(scr, (FIELD_LEFT + FIELD_CELL_WIDTH * cell[0], FIELD_TOP))

            scr = pygame.Surface((FIELD_CELL_WIDTH * FIELD_WIDTH, FIELD_CELL_HEIGHT))
            scr.set_alpha(128)
            scr.fill(pygame.Color(255, 255, 0))
            screen.blit(scr, (FIELD_LEFT, FIELD_TOP + FIELD_CELL_HEIGHT * cell[1]))

    def get_click(self, mouse_pos, checkPlant, objec):
        cell = self.get_cell(mouse_pos)
        i = 0
        while i < len(self.objects) + len(objec):
            if i < len(self.objects) and self.objects[i][0].type == 'sun' and self.objects[i][0].rect.collidepoint(mouse_pos):
                self.board[self.objects[i][2]][self.objects[i][3]].objects[self.objects[i][4]].active = False
                self.objects.pop(i)
            elif i >= len(self.objects) and objec[i - len(self.objects)].type == 'sun' and objec[i - len(self.objects)].rect.collidepoint(mouse_pos):
                objec[i - len(self.objects)].active = False
                i += 1
            else:
                i += 1
        if cell and checkPlant:
            temp = self.on_click(cell, checkPlant)
            if temp[0]:
                return [True, self.game.suns - temp[1], objec]
        return [False, self.game.suns, objec]

    def on_click(self, cell, checkPlant):
        if self.board[cell[0]][cell[1]] == '':
            self.board[cell[0]][cell[1]] = choicePlant(checkPlant[0], [cell[0], cell[1]], self.game)
            return [True, checkPlant[1]]
        return [False, 0]

    def get_cell(self, mouse_pos):
        self.data.clear()
        if self.left < mouse_pos[0] < self.left + self.width * self.cell_width \
                and self.top < mouse_pos[1] < self.top + self.height * self.cell_height:
            self.data.append((mouse_pos[0] - self.left) // self.cell_width)
            self.data.append((mouse_pos[1] - self.top) // self.cell_height)
            return self.data
        else:
            return None
