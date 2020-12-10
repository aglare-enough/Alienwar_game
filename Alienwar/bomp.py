import pygame
class Bomp:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.image1=pygame.image.load('bomp1.png')
        self.image2=pygame.image.load('bomp2.png')
        self.image3=pygame.image.load('bomp3.png')
        self.image4=pygame.image.load('bomp4.png')
        self.image5=pygame.image.load('bomp5.png')
        self.images=[self.image1,self.image2,self.image3,self.image4,self.image5]
    def draw_image(self,x,y,count):
        self.rect=pygame.Rect(x,y,40,40)
        self.screen.blit(self.images[count],self.rect)
