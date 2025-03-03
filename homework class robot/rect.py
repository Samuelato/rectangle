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

rect1=Rectangle("black",35,35,35,0)
rect2=Rectangle("white",35,35,0,0)
rect3=Rectangle("white",35,35,70,0)
rect4=Rectangle("black",35,35,105,0)
rect5=Rectangle("white",35,35,140,0)
rect6=Rectangle("black",35,35,0,35)
rect7=Rectangle("white",35,35,35,35)
rect8=Rectangle("black",35,35,70,35)

#game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill("green") 
    rect1.draw()
    rect2.draw()
    rect3.draw()
    rect4.draw()
    rect5.draw()
    rect6.draw()
    rect7.draw()
    rect8.draw()
    DeprecationWarning
    pygame.display.update()

pygame.quit()