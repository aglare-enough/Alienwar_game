import pygame
class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.image=pygame.image.load('yasuo.jpg')
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.rstate=0
        self.lstate=0
        self.upstate=0
        self.dwstate=0
    def blitme(self):
        self.screen.blit(self.image,self.rect)