import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.image=pygame.image.load('wind.png')
        self.rect=self.image.get_rect()
        self.rect.midtop=ai_game.ship.rect.midtop
        self.y=float(self.rect.y)
    def update(self):
        self.y-=self.settings.bullet_speed
        self.rect.y=self.y
    def drawit(self):
        self.screen.blit(self.image,self.rect)
class Skill(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.skill_image=pygame.image.load('skill_wind.png')
        self.settings=ai_game.settings
        self.rect=pygame.Rect(0,0,60,100)
        self.rect.midtop=ai_game.ship.rect.midtop
    def skill_update(self):
        self.rect.y-=self.settings.bullet_speed*2
    def blitit(self):
        self.screen.blit(self.skill_image,self.rect)