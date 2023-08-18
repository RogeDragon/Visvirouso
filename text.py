import pygame

pygame.font.init()

def display_text(value, display, offset):

    font = pygame.font.SysFont("monospace", 30)
    text = font.render(value, 1, (255, 255,255))

    display.blit(text, (200 + offset[0], 20 + offset[1]))

def letter_text(value, display, offset):

    font = pygame.font.SysFont("monospace", 10)
    text = font.render(value, 1, (255, 255,255))

    display.blit(text, (offset[0] - 3, 380 + offset[1]))