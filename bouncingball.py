from turtle import Screen
from pygame import Vector2,Color,mixer
import pygame
pygame.init()
background_color= (0,0,0)
white=(255,255,255)

window=pygame.display.set_mode((500,900))
pygame.display.set_caption("Bouncy")
mixer.init()
sound = mixer.Sound("jump.wav")

running=True;

class Ball:
    def __init__(self):
        self.position=Vector2(230,330)
        self.color=(0,0,0)
        self.gravity=Vector2(0,0,23)
        self.velocity=Vector2(-7,-7)
        self.prevpos=Vector2(self.position.x, self.position.y)
        self.radius = 30


    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(Screen,self.position.x,self.position.y)

        self.velocity += self.gravity
        self.position += self.velocity

    


ball=Ball()
color=Color(255,255,255)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    window.fill(background_color)
    pygame.draw.ellipse(window,white,(0,200,500,500),5)



    pygame.display.update()

pygame.quit()