#make snake object
#move circle based on coordinates

import pygame;
pygame.init();
screen = pygame.display.set_mode((1280, 720));
clock = pygame.time.Clock();
running = True;
dt = 0;
numRows, numCols = 15,15;


class Grid:
    def __init__(self,r,c):
        self.numRows = r;
        self.numCols = c;
        self.cellWidth = screen.get_width()/r;
        self.cellLength = screen.get_height()/c;
        self.snakeHead = SnakeSegment(self.getLocationX(self.numRows//2),self.getLocationY(self.numCols//2));

    def getLocationY(self,row):
        return (self.cellLength*row) + (self.cellLength//2);

    def getLocationX (self, col):
        return (self.cellWidth*col) + (self.cellWidth//2);

    def changeDirection (memyselfandi, dir):
        memyselfandi.snakeHead.direction = dir;

    def tick(self):
        self.snakeHead.moveDir();




class SnakeSegment:
    def __init__(self, x, y):
        self.snake_pos = pygame.Vector2(x,y);
        self.direction = "y+";

    def moveDir(self,speed=.5):
        dir = self.direction;
        if dir=="y+":
            self.snake_pos.y += speed;
        elif dir =="y-":
            self.snake_pos.y-=speed;
        elif dir =="x+":
            self.snake_pos.x+=speed;
        else:
            self.snake_pos.x-=speed;


snakeGrid = Grid(10,10);


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
    screen.fill("blue")
    a = pygame.Rect(snakeGrid.snakeHead.snake_pos, (250, 50));
    pygame.draw.ellipse(screen, "pink", a) ;

    keys = pygame.key.get_pressed()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snakeGrid.changeDirection("y-");
    if keys[pygame.K_s]:
        snakeGrid.changeDirection ("y+");
    if keys[pygame.K_a]:
        snakeGrid.changeDirection("x-");
    if keys[pygame.K_d]:
        snakeGrid.changeDirection ("x+");

    snakeGrid.tick() #move

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
