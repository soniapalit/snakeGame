#make snake object
#move circle based on coordinates

import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
numRows, numCols = 15,15;


class Grid:
    def __init__(self,r,c):
        self.numRows = r;
        self.numCols = c;
        self.cellWidth = screen.get_width()/r;
        self.cellLength = screen.get_height()/c;
        self.snakeHead = SnakeSegment(self.getLocation(self.numRows//2),self.getLocation(self.numCols//2));

    def getLocationY(self,row):
        return (self.cellLength*row) + (self.cellLength//2);

    def getLocationX (self, col):
        return (self.cellWidth*col) + (self.cellWidth//2);



class SnakeSegment:
    def __init__(self, x, y):
        self.snake_pos = pygame.Vector2(x,y)
        self.direction = "y+"

    def moveDir(self):
        dir = self.direction
        speed=.5
        if dir=="y+":
            self.snake_pos.y += speed
        elif dir =="y-":
            self.snake_pos.y-=speed
        elif dir =="x+":
            self.snake_pos.x+=speed
        else:
            self.snake_pos.x-=speed

    def moveDir(self,speed):
        dir = self.direction
        if dir=="y+":
            self.snake_pos.y += speed
        elif dir =="y-":
            self.snake_pos.y-=speed
        elif dir =="x+":
            self.snake_pos.x+=speed
        else:
            self.snake_pos.x-=speed


snakeGrid = Grid(10,10);
s = SnakeSegment();


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("blue")
    a = pygame.Rect(s.snake_pos, (250, 50))
    pygame.draw.ellipse(screen, "pink", a) 

    keys = pygame.key.get_pressed()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        s.direction="y-"
    if keys[pygame.K_s]:
        s.direction = "y+"
    if keys[pygame.K_a]:
        s.direction = "x-"
    if keys[pygame.K_d]:
        s.direction = "x+"

    s.moveDir(1) #move

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
