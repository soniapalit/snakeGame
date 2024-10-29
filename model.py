#make snake object
#move circle based on coordinates
import time
import pygame;
import random;
import params;

pygame.init();
screen = pygame.display.set_mode((params.screenW, params.screenH)); #(600, 400))#
clock = pygame.time.Clock();
running = True;
dt = 0;

rotation = 0;

class food:
    def __init__(self, posi):
        self.item = "apple"
        self.pos = posi
    def drawFood(self):
        foodSHape = pygame.Rect(self.pos, (params.cellWidth,params.cellLength))
        pygame.draw.ellipse(screen, "red", foodSHape)
    def eatFood(self):
        #self-destroy? idk
        pass


class Grid:
    def __init__(self):
        self.snakeHead = SnakeSegment(self.getLocationX(params.numRows//2),self.getLocationY(params.numCols//2));
        self.currentDir = "y+"
        self.foodlist = []
    

    def getLocationY(self,row):
        return (params.cellLength*row) + (params.cellLength//2);

    def getLocationX (self, col):
        return (params.cellWidth*col) + (params.cellWidth//2);

    def changeDirection (self, dir):
        print("direction changed")
        self.currentDir = dir

    def tick(self):
       #check snake segment location
       #make if statements for each directions=
        colRand = random.randint(0,params.numCols);
        rowRand = random.randint(0,params.numRows);
        v = pygame.Vector2(self.getLocationX(colRand), self.getLocationY(rowRand));

        create = False;
        x1 = self.snakeHead.getX()
        y1 = self.snakeHead.getY()

        global rotation
        if rotation == 1:
            f = food(v)
            self.foodlist.append(f)
        if self.currentDir=="y+":
            self.snakeHead.moveDir(self.snakeHead.getX(), self.snakeHead.getY()+params.cellLength)
        elif self.currentDir =="y-":
            self.snakeHead.moveDir(self.snakeHead.getX(), self.snakeHead.getY()-params.cellLength)
        elif self.currentDir =="x+":
            self.snakeHead.moveDir(self.snakeHead.getX()+params.cellWidth, self.snakeHead.getY())
        else:
            self.snakeHead.moveDir(self.snakeHead.getX()-params.cellWidth, self.snakeHead.getY())
        rotation+=1;
        rotation %= 8





def intersect (x1,y1,w1,h1,x2,y2,w2,h2):
    xInt, yInt = False, False;
    if x2>x1:
        if (x1+w1)>x2:
            xInt = True
    elif x1>x2:
        if x2+w2 > x1:
            xInt = True
    
    if y2>y1:
        if (y1+h1)>y2:
            yInt = True
    elif y1>y2:
        if y2+h2 > y1:
            yInt = True
    return xInt and yInt;


class SnakeSegment:
    def __init__(self, x, y):
        self.snake_pos = pygame.Vector2(x,y);
        self.next = None

    def getY(self):
        return self.snake_pos.y
    
    def getX (self):
        return self.snake_pos.x
    
    ##next segment? the fancy list thing? i don't rememeber how to

    def moveDir(self, newX, newY, create=False):
        oldLoc =self.snake_pos
        self.snake_pos = pygame.Vector2(newX, newY)

        if self.next is not None:
            self.next.moveDir(oldLoc.x, oldLoc.y, create=True)
        else: # we are the last node
            if create:
                self.next = SnakeSegment(oldLoc.x,oldLoc.y)
                nextBody = pygame.Rect(self.next.snake_pos, (params.cellWidth,params.cellLength))
                pygame.draw.ellipse(screen, "pink",nextBody)



def draw_snake(snake_head, num):
    print(num)
    # draw the current segment
    numm = num*params.cellLength
    a = pygame.Rect(snake_head.snake_pos, (params.cellWidth, params.cellLength))
    pygame.draw.ellipse(screen, "pink", a)

    if not snake_head.next == None:
        draw_snake(snake_head.next, num+1)




snakeGrid = Grid();


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
    
    for foods in snakeGrid.foodlist:
        foods.drawFood();

    draw_snake(snakeGrid.snakeHead,1)
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    time.sleep(1)

pygame.quit()
