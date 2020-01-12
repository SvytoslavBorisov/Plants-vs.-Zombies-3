import pygame
from allConstants import *


class AlmanahZombie:

    def __init__(self, width, height, cell_width, cell_height, left, top, step_top, step_left, screen):
        self.width = width
        self.height = height
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.left = left
        self.top = top
        self.checkPlant = [[], 0, 0, '']
        self.screen = screen
        self.step_top = step_top
        self.step_left = step_left
        self.board = []
        self.board.append([])
        self.board[0].append(['normal', False])
        self.board[0].append(['normalWithFlag', False])
        self.board[0].append(['bucket', False])
        self.board.append([])
        self.board[1].append(['konus', False])
        self.data = []

    def render(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j][1]:
                    self.screen.blit(cards[self.board[i][j][0]], (self.cell_width * j + self.left + self.step_left * j,
                                                                  self.cell_height * i + self.top + self.step_top * i,
                                                                  self.cell_width,
                                                                  self.cell_height))
                else:
                    self.screen.blit(cards[self.board[i][j][0]], (self.cell_width * j + self.left + self.step_left * j,
                                                                  self.cell_height * i + self.top + self.step_top * i,
                                                                  self.cell_width,
                                                                  self.cell_height))
        if self.checkPlant[0] != []:
            self.screen.blit(self.checkPlant[0][self.checkPlant[2]], (650, 120))
            i = 0
            for x in almanac_text[self.checkPlant[3]]:
                self.screen.blit(x, (600, 314 + i * 18))
                i += 1
            self.checkPlant[2] += 1
            if self.checkPlant[2] >= self.checkPlant[1]:
                self.checkPlant[2] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell):
        if cell[1] < len(self.board) and cell[0] < len(self.board[cell[1]]):
            self.returnSostoynie()
            self.board[cell[1]][cell[0]][1] = True
            self.checkPlant = [zombies[self.board[cell[1]][cell[0]][0]], len(zombies[self.board[cell[1]][cell[0]][0]]), 0, self.board[cell[1]][cell[0]][0]]


    def get_cell(self, mouse_pos):
        self.data.clear()
        if self.left < mouse_pos[0] < self.left + self.width * self.cell_width + self.width * self.step_left\
                and self.top < mouse_pos[1] < self.top + self.height * self.cell_height + self.height * self.step_top:
            self.data.append((mouse_pos[0] - self.left) // (self.cell_width + self.step_left))
            self.data.append((mouse_pos[1] - self.top) // (self.cell_height + self.step_top))
            return self.data
        else:
            return None

    def returnSostoynie(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j][1] = False