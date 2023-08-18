import pygame, sys
import save, text
import time

from grid import Grid

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

class main:
    def __init__ (self):
        pygame.display.set_caption("Track Maker")
        Window_Size = (400, 400)
        self.gh = 23
        self.gw = 12
        self.gSize = 16
        self.play = False
        self.convert_tracks = False

        self.track = 1
        self.screen = pygame.display.set_mode(Window_Size, 0, 32)

        self.grid = Grid(self.gh, self.gw, self.gSize, self.gSize, self.screen)
        self.converted = save.convert(self.grid.button_list)
        self.change_track = False

        self.sound = []

        for m in range(12):
            self.sound.append(pygame.mixer.Sound("soundSamples/" + str(m) + ".wav"))

        #a dictionary of tracks
        self.save_dict = {"1": save.convert(Grid(self.gh, self.gw, self.gSize, self.gSize, self.screen).button_list),
                          "2": save.convert(Grid(self.gh, self.gw, self.gSize, self.gSize, self.screen).button_list),
                          "3": save.convert(Grid(self.gh, self.gw, self.gSize, self.gSize, self.screen).button_list)}

        self.play_track_1 = save.button_convert(self.save_dict, str(1), self.gSize, self.screen, self.gSize)
        self.play_track_2 = save.button_convert(self.save_dict, str(2), self.gSize, self.screen, self.gSize)
        self.play_track_3 = save.button_convert(self.save_dict, str(3), self.gSize, self.screen, self.gSize)
    def update(self):
        while True:
            self.screen.fill(0)
            self.grid.update()

            if self.convert_tracks == True:
                self.play_track_1 = save.button_convert(self.save_dict, str(1), self.gSize, self.screen, self.gSize)
                self.play_track_2 = save.button_convert(self.save_dict, str(2), self.gSize, self.screen, self.gSize)
                self.play_track_3 = save.button_convert(self.save_dict, str(3), self.gSize, self.screen, self.gSize)
                self.convert_tracks = False

            if self.play == False:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_s:
                            save.save(self.save_dict)
                        if event.key == K_l:
                            self.save_dict = save.load()
                            self.grid.button_list = save.button_convert(self.save_dict, str(self.track), self.gSize, self.screen, self.gSize)
                        if event.key == K_d:
                            self.save_dict[str(self.track)] = save.convert(Grid(self.gh, self.gw, self.gSize, self.gSize, self.screen).button_list)
                            self.grid.button_list = save.button_convert(self.save_dict, str(self.track), self.gSize, self.screen, self.gSize)
                            print("del")
                        if event.key == K_p:
                            self.play = True
                            self.convert_tracks = True

                        #changes the tracks
                        if event.key == K_1:
                            self.track = 1
                            self.change_track = True
                        if event.key == K_2:
                            self.track = 2
                            self.change_track = True
                        if event.key == K_3:
                            self.track = 3
                            self.change_track = True

                #takes just converts the track
                if self.change_track:
                    if self.track == 1:
                        self.grid.button_list = save.button_convert(self.save_dict, str(self.track), self.gSize, self.screen, self.gSize)
                    elif self.track == 2:
                        self.grid.button_list = save.button_convert(self.save_dict, str(self.track), self.gSize, self.screen, self.gSize)
                    else:
                        self.grid.button_list = save.button_convert(self.save_dict, str(self.track), self.gSize, self.screen, self.gSize)
                    self.change_track = False

                # stores it in the dictionary
                if self.track == 1:
                    self.save_dict["1"] = save.convert(self.grid.button_list)
                elif self.track == 2:
                    self.save_dict["2"] = save.convert(self.grid.button_list)
                else:
                    self.save_dict["3"] = save.convert(self.grid.button_list)
            else:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_p:
                            if self.play == True:
                                self.play = False

                for i in range(self.gh):
                    time.sleep(1)
                    for row in self.play_track_1:
                        for index, button in enumerate(row):
                            if button.selected == True:
                                self.sound[index].play()
                        time.sleep(0.1)

                    for row in self.play_track_2:
                        for index, button in enumerate(row):
                            if button.selected == True:
                                self.sound[index].play()
                        time.sleep(0.1)

                    for row in self.play_track_3:
                        for index, button in enumerate(row):
                            if button.selected == True:
                                self.sound[index].play()
                        time.sleep(0.1)


            text.display_text("S-Save", self.screen, (20, 0))
            text.display_text("L-Load", self.screen, (20, 40))
            text.display_text("D-Delete", self.screen, (20, 80))
            text.display_text("P-Play", self.screen, (20, 120))
            text.display_text("Track: " + str(self.track), self.screen, (20, 160))

            for i in range(7):
                text.letter_text(chr(i + 65), self.screen, ((i *2)* self.gSize, 0))

            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
   main = main()
   main.update()