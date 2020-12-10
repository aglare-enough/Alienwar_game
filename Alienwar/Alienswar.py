import pygame
import sys
from time import sleep
from random import randint
from settings import Settings
from ship_mod_blit import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from bullet import Skill
from game_information import Information
from bomp import Bomp
game_state=0
menu=0
game=1
over=2
score=0
class Alienwar_game:
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.ship=Ship(self)
        self.button=Button(self,"start play")
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self.skills=pygame.sprite.Group()
        pygame.display.set_caption('诺克萨斯入侵')
        self.creat_alien()
        self.move=list()
        self.lives=self.settings.ship_lives
        self.information=Information(self)
        self.bomp=Bomp(self)
        self.clock=pygame.time.Clock()
        self.time=60
    def creat_alien(self):
        available_space_x=self.settings.screen_width-2*40
        avaliable_space_y=self.settings.screen_height-2*40
        number_alien_x=available_space_x//80
        for alien_number in range(number_alien_x):
            new_alien=Alien(self)
            new_alien.rect.x=randint(0,1000)
            new_alien.rect.y=randint(0,200)
            self.aliens.add(new_alien)
    def fire(self):
        if len(self.bullets)<self.settings.bullet_maxnum:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    def fire_skill(self):
        newskill=Skill(self)
        self.skills.add(newskill)
    def event_check(self):
        global score
        global game_state
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                sys.exit()
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_a or event.key==pygame.K_LEFT ):
                    self.ship.lstate=1
                if(event.key==pygame.K_d or event.key ==pygame.K_RIGHT):
                    self.ship.rstate=1
                if event.key==pygame.K_j:
                    self.fire()
                if event.key==pygame.K_k:
                    self.fire_skill()
            if(event.type==pygame.KEYUP):
                if(event.key==pygame.K_a or event.key==pygame.K_LEFT):
                    self.ship.lstate=0
                if(event.key==pygame.K_d or event.key==pygame.K_RIGHT):
                    self.ship.rstate=0
            if(event.type==pygame.MOUSEBUTTONDOWN):
                mouse_pos=pygame.mouse.get_pos()
                if game_state==2:
                    if self.screen.get_rect().collidepoint(mouse_pos):
                        game_state=menu
                        score=0
                elif game_state==0:
                    if self.button.rect.collidepoint(mouse_pos):
                        game_state = game
                        self.lives=self.settings.ship_lives
    def run_game(self):
        global game_state
        global score
        count=0
        count1=0
        while True:
            self.clock.tick(self.time)
            self.screen.fill(self.settings.bg_color)
            self.event_check()
            if game_state==menu:
                self.screen.blit(self.button.msg_image,self.button.rect)
            elif game_state==game:
                for number in range(self.lives):
                    self.screen.blit(self.ship.image,pygame.Rect(number*40,0,40,40))
                self.button.label1()
                i=0
                if self.ship.rect.x>=self.settings.ship_speed:
                    if self.ship.lstate == 1:
                        self.ship.rect.x -= self.settings.ship_speed
                if self.ship.rect.x<=self.settings.screen_width-self.settings.ship_speed-40:
                    if self.ship.rstate==1:
                        self.ship.rect.x+=self.settings.ship_speed
                self.bullets.update()
                self.ship.blitme()
                for bullet in self.bullets.sprites():
                    bullet.drawit()
                    if bullet.y<=0:
                        self.bullets.remove(bullet)
                for skill in self.skills.sprites():
                    skill.skill_update()
                    skill.blitit()
                    if skill.rect.y<=0:
                        self.skills.remove(skill)
                for num in range(len(self.aliens)):
                    self.move.append(1)
                for alien in self.aliens.sprites():
                    if alien.rect.left==self.screen.get_rect().left or alien.rect.right==self.screen.get_rect().right:
                        self.move[i]=-self.move[i]
                    alien.rect.x+=self.settings.alien_speed*self.move[i]
                    alien.rect.y+=self.settings.alien_speed_y
                    i+=1
                    if alien.rect.left<self.screen.get_rect().left:
                        alien.rect.left=self.screen.get_rect().left
                    if alien.rect.right>self.screen.get_rect().right:
                        alien.rect.right=self.screen.get_rect().right
                    if alien.rect.centery>=self.screen.get_rect().bottom:
                        print("诺手打进你家了！！！")
                        sleep(1.5)
                        self.bullets.empty()
                        self.aliens.empty()
                        self.creat_alien()
                        self.lives-=1
                        break
                for alien_self in self.aliens.sprites():
                    for bullet_self in self.bullets.sprites():
                        if pygame.sprite.collide_rect(alien_self,bullet_self):
                            x=alien_self.rect.x
                            y=alien_self.rect.y
                        if pygame.sprite.collide_rect(alien_self,bullet_self) or count!=0 and count<=100:
                            self.bomp.draw_image(x,y,count1%5)
                            count+=1
                            if(count%20==0):
                                count1+=1
                        if count>100:
                            count=0
                collision=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
                collision2=pygame.sprite.groupcollide(self.skills,self.aliens,False,True)
                if collision:
                    score+=self.settings.alien_score
                if collision2:
                    score+=self.settings.alien_score*len(collision2.values())
                self.information.draw_score('score: '+str(score))
                self.screen.blit(self.information.score_image,self.information.score_image_rect)
                if not self.aliens:
                    self.bullets.empty()
                    self.skills.empty()
                    self.creat_alien()
                    self.settings.alien_speed+=1
                if pygame.sprite.spritecollideany(self.ship,self.aliens):
                    print("亚索被诺手打死了 !!!")
                    sleep(1.5)
                    self.ship.rect.midbottom=self.screen.get_rect().midbottom
                    self.bullets.empty()
                    self.aliens.empty()
                    self.creat_alien()
                    self.lives-=1
                if self.lives==0:
                    game_state=over
                self.aliens.draw(self.screen)
            elif game_state == over:
                self.button.label2()
                self.button.label3(str(score))
            pygame.display.flip()
if __name__=='__main__':
    ai_game=Alienwar_game()
    ai_game.run_game()