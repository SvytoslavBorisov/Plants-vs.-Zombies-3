import pygame
from allConstants import *

class Panel:
    def __init__(self, height, cell_width, cell_height, left, top, step, screen, game):
        self.width = 1
        self.height = height
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.left = left
        self.top = top
        self.checkPlant = ''
        self.screen = screen
        self.step = step
        self.game = game
        self.board = [[]]
        self.board[0].append(['gatlingPea', 100, False])
        self.board[0].append(['sunrise', 50, False])
        self.board[0].append(['wallNut', 50, False])
        self.board[0].append(['potatoBomb', 25, False])
        self.board[0].append(['squash', 75, False])
        #self.board[0].append(['cabbage', 175, False])
        self.data = []

    def render(self):
        for i in range(self.height):
            for j in range(self.width):

                if self.board[j][i][0] != '':

                    if self.board[j][i][2]:
                        self.screen.blit(cards[self.board[j][i][0]], (self.cell_width * j + self.left,
                                               self.cell_height * i + self.top + self.step * i,
                                               self.cell_width,
                                               self.cell_height))
                        self.screen.blit(punkteer, (self.cell_width * j + self.left,
                                               self.cell_height * i + self.top + self.step * i,
                                               self.cell_width,
                                               self.cell_height))
                    else:
                        if self.game.suns >= self.board[j][i][1]:
                            self.screen.blit(cards[self.board[j][i][0]], (self.cell_width * j + self.left,
                                                                      self.cell_height * i + self.top + self.step * i,
                                                                      self.cell_width,
                                                                      self.cell_height))
                        else:
                            self.screen.blit(cards[self.board[j][i][0]], (self.cell_width * j + self.left,
                                                                          self.cell_height * i + self.top + self.step * i,
                                                                          self.cell_width,
                                                                          self.cell_height))
                            scr = pygame.Surface((self.cell_width, self.cell_height))
                            scr.set_alpha(128)
                            scr.fill(pygame.Color(64, 64, 64))
                            self.screen.blit(scr, (self.left + j * self.cell_width, self.top + i * self.cell_height + self.step * i))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell):
        if self.game.suns >= self.board[cell[0]][cell[1]][1]:
            self.checkPlant = self.board[cell[0]][cell[1]]
            self.returnSostoynie()
            self.board[cell[0]][cell[1]][2] = True

    def get_cell(self, mouse_pos):
        self.data.clear()
        if self.left < mouse_pos[0] < self.left + self.width * self.cell_width \
                and self.top < mouse_pos[1] < self.top + self.height * self.cell_height + self.step:
            self.data.append((mouse_pos[0] - self.left) // self.cell_width)
            self.data.append((mouse_pos[1] - self.top) // (self.cell_height + self.step))
            return self.data
        else:
            return None

    def returnSostoynie(self):
        for i in range(len(self.board[0])):
            self.board[0][i][2] = False