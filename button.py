import pygame

class Button():
    def __init__(self, pos, selected, size, display):
        self.selected = selected
        self.mousepos = [0, 0]
        self.rect = pygame.Rect(pos[0], pos[1], size, size)
        self.display = display
        self.timer = 0

    def update(self):
        self.timer += 0.1
        self.mousepos = pygame.mouse.get_pos()

        if self.selected == True:  #a way to check the colour of the  sprite
            pygame.draw.rect(self.display, 1, self.rect)
        elif self.selected == False:
            pygame.draw.rect(self.display, (255, 255, 255), self.rect)

        if self.rect.collidepoint(self.mousepos[0], self.mousepos[1]):
            if self.timer >= 1:
                if pygame.mouse.get_pressed()[0]:
                    if self.selected:
                        self.selected = False
                        self.timer = 0
                    else:
                        self.selected = True
                        self.timer = 0