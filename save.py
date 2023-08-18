import pygame
from button import Button
import json

def convert(current):
    listy = []
    for row in current:
        rowy = []
        for button in row:
            if button.selected == False:
                rowy.append(0)
            else:
                rowy.append(1)
        listy.append(rowy)

    return listy

def button_convert(dict, index, displace, display, size):
    button_list = []
    for x, row in enumerate(dict[index]):
        grid_list = []
        for y, tile in enumerate(row):
            if tile == 1:
                grid_list.append(Button((y * displace, x * displace), True, size, display))
            else:
                grid_list.append(Button((y * displace, x * displace), False, size, display))
        button_list.append(grid_list)
    return button_list
def save(track):
    json_file = json.dumps(track)

    with open("store.json", "w") as outfile:
        outfile.write(json_file)
    print("saved")

def load():
    with open('store.json', 'r') as openfile:
        track = json.load(openfile)
    return track