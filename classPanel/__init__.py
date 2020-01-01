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
        self.board[0].append(['gatlingPea', 100, False, 1, 140])
        self.board[0].append(['sunrise', 50, False, 140, 140])
        self.board[0].append(['wallNut', 50, False, 1, 140])
        self.board[0].append(['potatoBomb', 25, False, 1, 140])
        self.board[0].append(['squash', 75, False, 1, 140])
        #self.board[0].append(['cabbage', 175, False, 1])
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
                        self.screen.blit(gamesSprites['punkteer'], (self.cell_width * j + self.left,
                                               self.cell_height * i + self.top + self.step * i,
                                               self.cell_width,
                                               self.cell_height))
                    else:
                        if self.game.suns >= self.board[j][i][1] and self.board[j][i][3] == self.board[j][i][4]:
                            self.screen.blit(cards[self.board[j][i][0]], (self.cell_width * j + self.left,
                                                                      self.cell_height * i + self.top + self.step * i,
                                                                      self.cell_width,
                                                                      self.cell_height))
                        else:
                            self.screen.blit(cards[self.board[j][i][0]], (self.cell_width * j + self.left,
                                                                          self.cell_height * i + self.top + self.step * i,
                                                                          self.cell_width,
                                                                          self.cell_height))
                            self.board[j][i][3] += 1
                            if self.board[j][i][4] <= self.board[j][i][3] + 10:
                                self.board[j][i][3] = self.board[j][i][4]
                            else:
                                scr = pygame.Surface((self.cell_width - 7, 75 / self.board[j][i][4] * self.board[j][i][3]))
                                scr.set_alpha(160)
                                scr.fill(pygame.Color(64, 64, 64))
                                self.screen.blit(scr, (self.left + j * self.cell_width + 5,
                                                       self.top + i * self.cell_height + self.step * i + 75 -
                                                       75 / self.board[j][i][4] * self.board[j][i][3] - 2))

    def mouse_move(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            if self.game.suns < self.board[cell[0]][cell[1]][1]:
                screen.blit(descriptionNoSun[self.board[cell[0]][cell[1]][0]], (PANEL_LEFT + PANEL_CELL_WIDTH, PANEL_TOP + PANEL_CELL_HEIGHT * cell[1] + cell[1] * PANEL_STEP))
            elif self.board[cell[0]][cell[1]][4] != self.board[cell[0]][cell[1]][3]:
                screen.blit(descriptionNoTime[self.board[cell[0]][cell[1]][0]], (
                PANEL_LEFT + PANEL_CELL_WIDTH, PANEL_TOP + PANEL_CELL_HEIGHT * cell[1] + cell[1] * PANEL_STEP))
            else:
                screen.blit(description[self.board[cell[0]][cell[1]][0]], (
                PANEL_LEFT + PANEL_CELL_WIDTH, PANEL_TOP + PANEL_CELL_HEIGHT * cell[1] + cell[1] * PANEL_STEP))


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell):
        if self.game.suns >= self.board[cell[0]][cell[1]][1] and self.board[cell[0]][cell[1]][3] == self.board[cell[0]][cell[1]][4]:
            self.checkPlant = self.board[cell[0]][cell[1]]
            self.returnSostoynie(False)
            self.board[cell[0]][cell[1]][2] = True

    def get_cell(self, mouse_pos):
        self.data.clear()
        if self.left < mouse_pos[0] < self.left + self.width * self.cell_width \
                and self.top < mouse_pos[1] < self.top + self.height * self.cell_height + self.height * self.step:
            self.data.append((mouse_pos[0] - self.left) // self.cell_width)
            self.data.append((mouse_pos[1] - self.top) // (self.cell_height + self.step))
            return self.data
        else:
            return None

    def returnSostoynie(self, x):
        for i in range(len(self.board[0])):
            if self.board[0][i][2] and x:
                self.board[0][i][3] = 1
            self.board[0][i][2] = False