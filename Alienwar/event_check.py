import pygame
class Event:
    def __init__(self,ai_game):
        self.event=ai_game.pygame.event.get()
    def key_down(self):
        for event in self.event:
            if()