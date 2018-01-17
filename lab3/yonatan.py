from turtle import *
import time
import random
colormode(255)

class Ball(Turtle):
    def __init__(self, x,y,dx,dy,r):
        Turtle.__init__(self)
        self.pu()
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.shape("circle")
        self.shapesize(r/10)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.color(r,g,b)
    def move(self,screen_width, screen_hight):
        current_x = self.xcor()
        new_x = current_x + self.dx
        current_y = self.ycor()
        new_y = current_y + self.dy
        right_side_ball = new_x + self.r
        left_side_ball = new_x - self.r
        bottom_ball = new_y - self.r
        upper_ball_side = new_y + self.r
        self.goto(new_x, new_y)
        if bottom_ball < -screen_hight/2 or upper_ball_side > screen_hight/2:
            self.dy *= -1
        if left_side_ball < -screen_width/2 or right_side_ball > screen_width/2:
            self.dx *= -1

tracer(0)
ht()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2

MY_BALL = (0,0,0.5,-0.4,30)
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range(NUMBER_OF_BALLS):
    x = random.randint(int(- SCREEN_WIDTH / 2 + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH/2 - MAXIMUM_BALL_RADIUS))
    y = random.randint(-SCREEN_HEIGHT/2 + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT/2 - MAXIMUM_BALL_RADIUS)
    dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
    dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
    r = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
    while dx == 0:
        dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
    while dy == 0:
        dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
    new_ball = Ball(x,y,dx,dy,r)
    BALLS.append(new_ball)

def move_all_balls(BALLS):
    for index in range(len(BALLS)):
        BALLS[index].move(SCREEN_WIDTH , SCREEN_HEIGHT)

#move_all_balls(BALLS)

mainloop()
