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
    def getX(self):
        return self.pos.x;
    def getY(self):
        return self.pos.y;
    def drawFood(self):
        foodSHape = pygame.Rect(self.pos, (params.cellWidth,params.cellLength))
        pygame.draw.ellipse(screen, "red", foodSHape)
   


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
        self.currentDir = dir

    def tick(self):
       #check snake segment location
       #make if statements for each directions=
        colRand = random.randint(0,params.numCols);
        rowRand = random.randint(0,params.numRows);
        v = pygame.Vector2(self.getLocationX(colRand), self.getLocationY(rowRand));

        createMORE = False;
        x1 = self.snakeHead.getX()
        y1 = self.snakeHead.getY()
        w1 = params.cellWidth;
        h1 = params.cellLength;

        if not hitwall(x1,y1,w1,h1, snakeGrid.currentDir):

            for foodyum in self.foodlist:
                x2 = foodyum.getX()
                y2 = foodyum.getY()
                
                #right now i have h1, w1 = h2, w2 but that might change in future
                if intersect(x1,y1,w1,h1,x2,y2,h1,w1):
                    self.foodlist.remove(foodyum)
                    #print("INTERSECT WITH FOOD YAY")
                    createMORE = True


            global rotation
            print(len(self.foodlist))
            if len(self.foodlist) < 1:
                f = food(v)
                self.foodlist.append(f)
                len(self.foodlist)
            if rotation == 1:
                f = food(v)
                self.foodlist.append(f)

            if self.currentDir=="y+":
                self.snakeHead.moveDir(self.snakeHead.getX(), self.snakeHead.getY()+params.cellLength, create=createMORE)
            elif self.currentDir =="y-":
                self.snakeHead.moveDir(self.snakeHead.getX(), self.snakeHead.getY()-params.cellLength, create=createMORE)
            elif self.currentDir =="x+":
                self.snakeHead.moveDir(self.snakeHead.getX()+params.cellWidth, self.snakeHead.getY(), create=createMORE)
            else:
                self.snakeHead.moveDir(self.snakeHead.getX()-params.cellWidth, self.snakeHead.getY(), create=createMORE)
            rotation+=1;
            rotation %= 7

            createMORE = False
        else:
            screen.fill("red")
            print("wall hit")


def restartSnakeGameAww():
    global snakeGrid
    snakeGrid = Grid()
    screen.fill("blue")


def intersect (x1,y1,w1,h1,x2,y2,w2,h2):
    if x1 + w1 < x2 or x2 + w2 < x1:
        #if one is completely to the right/left of other
        return False;
    if y1 + h1 < y2 or y2 + h2 < y1:
        #if one is compeltely above/below other
        return False;
    return True;


def hitwall (x1,y1, w1, h1, moveDirection):
    if moveDirection == "y+":
        #going up
        if y1<=0:
            return True;
    if moveDirection == "y-":
        #going down
        if y1+h1>=params.screenH:
            return True;
    if moveDirection == "x+":
        #going right
        if x1+w1>=params.screenW:
            return True;
    if moveDirection == "x-":
        #going left
        if x1<=0:
            return True;


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
            self.next.moveDir(oldLoc.x, oldLoc.y, create=create)
        else: # we are the last node
            if create:
                self.next = SnakeSegment(oldLoc.x,oldLoc.y)
                nextBody = pygame.Rect(self.next.snake_pos, (params.cellWidth,params.cellLength))
                pygame.draw.ellipse(screen, "pink",nextBody)



def draw_snake(snake_head, num):
    if num == 1:
        color = "black"#make head a dif color for better gameplay i think
    else:
        color = "pink"
    ##print(num)
    # draw the current segment
    numm = num*params.cellLength
    a = pygame.Rect(snake_head.snake_pos, (params.cellWidth, params.cellLength))
    pygame.draw.ellipse(screen, color, a)

    if not snake_head.next == None:
        draw_snake(snake_head.next, num+1)



global snakeGrid
snakeGrid = Grid();


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
    
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                #print("w")
                snakeGrid.changeDirection("y-");
            if event.key==pygame.K_s:
                snakeGrid.changeDirection ("y+");
            
                #print("s")
            if event.key==pygame.K_a:
                snakeGrid.changeDirection("x-");
                #print("a")
            if event.key==pygame.K_d:
                snakeGrid.changeDirection ("x+");
                #print("d")

    screen.fill("blue")
    snakeGrid.tick() #move
    
    for foods in snakeGrid.foodlist:
        foods.drawFood();

    draw_snake(snakeGrid.snakeHead,1)
    
    pygame.display.flip()
    
    dt = clock.tick(100) / 1000
    time.sleep(.5)

    x1 = snakeGrid.snakeHead.getX()
    y1 = snakeGrid.snakeHead.getY()
    w1 = params.cellWidth
    h1 = params.cellLength

    if hitwall(x1, y1, w1, h1, snakeGrid.currentDir):
        time.sleep(2)
        restartSnakeGameAww()

pygame.quit()
