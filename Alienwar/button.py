import pygame
class Button:
    def __init__(self,ai_game,msg):
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.text_color=(200,180,190)
        self.width=200
        self.height=50
        self.button_color=(100,100,90)
        self.font=pygame.font.SysFont(None,48)
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        self.text=msg
        self._msg()
        self.label1_font=pygame.font.SysFont(None,32)
        self.label1_rect=pygame.Rect(10,40,80,40)
        self.label1_text="life number"
        self.label1_color=(180,100,100)
        self.label2_text="game over"
        self.label2_color=(0,0,0)
        self.label2_rect=pygame.Rect(0,0,self.width,self.height)
        self.label2_rect.center=self.screen_rect.center
        self.label3_font=pygame.font.SysFont(None,48)
        self.label3_text_color=(80,0,80)
        self.label3_rect=pygame.Rect(0,0,300,80)
        self.label3_rect.midtop=self.label2_rect.midbottom
        self.label3_text="your score:"
    def _msg(self):
        self.msg_image=self.font.render(self.text,True,self.text_color,self.button_color)
        self.msg_rect=self.msg_image.get_rect()
        self.msg_rect.center=self.rect.center
    def label1(self):
        self.label1_image=self.label1_font.render(self.label1_text,True,self.label1_color)
        self.label1_image_rect=self.label1_image.get_rect()
        self.label1_image_rect.center=self.rect.center
        self.screen.blit(self.label1_image,self.label1_rect)
    def label2(self):
        self.label2_image=self.label1_font.render(self.label2_text,True,self.label2_color)
        self.label2_image_rect=self.label2_image.get_rect()
        self.label2_image_rect.center=self.label2_rect.center
        self.screen.blit(self.label2_image,self.label2_rect)
    def label3(self,score):
        self.label3_image=self.label3_font.render(self.label3_text+score,True,self.label3_text_color)
        self.label3_image_rect=self.label3_image.get_rect()
        self.label3_image_rect.center=self.label3_rect.center
        self.screen.blit(self.label3_image,self.label3_rect)