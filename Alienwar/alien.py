import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image=pygame.image.load('nuoshou.jpg')
        self.rect=self.image.get_rect()


