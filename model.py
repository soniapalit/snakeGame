#make snake object
#move circle based on coordinates
import time
import pygame;
pygame.init();
screen = pygame.display.set_mode((1280, 720)); #(600, 400))#
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
        self.currentDir = "y+"
    

    def getLocationY(self,row):
        return (self.cellLength*row) + (self.cellLength//2);

    def getLocationX (self, col):
        return (self.cellWidth*col) + (self.cellWidth//2);

    def changeDirection (self, dir):
        print("direction changed")
        self.currentDir = dir

    def tick(self):

       #check snake segment location
       #make if statements for each directions=

        if self.currentDir=="y+":
            self.snakeHead.moveDir(self.snakeHead.getX(), self.snakeHead.getY()+self.cellLength)
        elif self.currentDir =="y-":
            self.snakeHead.moveDir(self.snakeHead.getX(), self.snakeHead.getY()-self.cellLength)
        elif self.currentDir =="x+":
            self.snakeHead.moveDir(self.snakeHead.getX()+self.cellWidth, self.snakeHead.getY())
        else:
            self.snakeHead.moveDir(self.snakeHead.getX()-self.cellWidth, self.snakeHead.getY())
    
    





class SnakeSegment:
    def __init__(self, x, y):
        self.snake_pos = pygame.Vector2(x,y);
        self.next = None

    def getY(self):
        return self.snake_pos.y
    
    def getX (self):
        return self.snake_pos.x
    
    ##next segment? the fancy list thing? i don't rememeber how to

    def moveDir(self, newX, newY, create=True):
        oldLoc =self.snake_pos
        self.snake_pos = pygame.Vector2(newX, newY)

        if self.next is not None:
            self.next.moveDir(oldLoc.x, oldLoc.y, create=True)
        else: # we are the last node
            if create:
                self.next = SnakeSegment(oldLoc.x,oldLoc.y)
                nextBody = pygame.Rect(self.next.snake_pos, (250,50))
                pygame.draw.ellipse(screen, "pink",nextBody)



def draw_snake(snake_head, num):
    print(num)
    # draw the current segment
    numm = num*snakeGrid.cellLength
    a = pygame.Rect(snake_head.snake_pos, (snakeGrid.cellWidth, snakeGrid.cellLength))
    pygame.draw.ellipse(screen, "pink", a)

    if not snake_head.next == None:
        draw_snake(snake_head.next, num+1)




snakeGrid = Grid(10,10);


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
    
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                print("w")
                snakeGrid.changeDirection("y-");
            if event.key==pygame.K_s:
                snakeGrid.changeDirection ("y+");
            
                print("s")
            if event.key==pygame.K_a:
                snakeGrid.changeDirection("x-");
                print("a")
            if event.key==pygame.K_d:
                snakeGrid.changeDirection ("x+");
                print("d")

    screen.fill("blue")
    snakeGrid.tick() #move
    
    draw_snake(snakeGrid.snakeHead,1)
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    time.sleep(1)

pygame.quit()
