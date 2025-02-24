import pygame
pygame.init()
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("Draw rectangle")


class Rectangle:
    def __init__(self,color,width,height,x,y):
        self.color=color
        self.width=width
        self.height=height
        self.x=x
        self.y=y
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.height,self.width))

rect1=Rectangle("black",70,30,300,200)

#game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill("green") 
    rect1.draw()
    pygame.display.update()

pygame.quit()