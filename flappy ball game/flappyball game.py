import pygame
pygame.init()
height=400
width=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("flappyball game")

clock=pygame.time.Clock()
gravity=2000
class Ball:
    def __init__(self,colour,size,x,y):
        self.x=x
        self.y=y
        self.size=size
        self.vy=0
        self.colour=colour
    def draw(self):
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.size)
circle=Ball("red",27,100,50)


running=True
while running:
    dt=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    circle.vy+=gravity*dt
    circle.y+=circle.vy*dt
    
    if circle.y>height-circle.radius:
    screen.fill("turquoise")
    circle.draw()
    pygame.display.update()
pygame.quit()