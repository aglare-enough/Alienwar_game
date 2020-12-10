import pygame
class Information:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.font=pygame.font.SysFont(None,48)
        self.score_rect=pygame.Rect(0,0,200,40)
        self.score_rect.topright=self.screen.get_rect().topright
        self.font_color=(100,120,120)
    def draw_score(self,text):
        self.score_image=self.font.render(text,True,self.font_color)
        self.score_image_rect=self.score_image.get_rect()
        self.score_image_rect.center=self.score_rect.center
