import pygame
from button import Button

class Grid():
    def __init__(self, rows, colums, size, displace, display):
        self.row = rows
        self.colums = colums
        self.size = size
        self.displace = displace
        self.display = display

        self.button_list = []

        for y in range(self.row):
            self.grid_list = []
            for x in range(self.colums):
                self.grid_list.append(Button((x * self.displace, y * self.displace), False, self.size, self.display))
            self.button_list.append(self.grid_list)

    def update(self):
        for row in self.button_list:
            for button in row:
                button.update()