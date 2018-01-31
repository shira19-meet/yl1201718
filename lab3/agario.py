from turtle import *
import turtle
import random
import time
from personalproject import Ball
import math
tracer(0)
hideturtle()

SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)

RUNNING=True
SLEEP=0.0077
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=15
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

My_Ball = Ball(30,"blue", 0,0,0,0)

def random_color(self):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    self.color((r,g,b))
Balls=[]
for i in range(NUMBER_OF_BALLS):
    x= random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS) 
    y= random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color= (random.random(), random.random(), random.random())
    ball=Ball(radius, color, x,y,dx,dy)
    Balls.append(ball)
    print(Balls)

def move_all_balls():
    for ball in Balls:
        ball.Move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
    if ball_a==ball_b:
        return False
    ball_ax=ball_a.xcor()
    ball_ay=ball_a.ycor()
    ball_bx=ball_b.xcor()
    ball_by=ball_b.ycor()
    ball_ar=ball_a.radius
    ball_br=ball_b.radius
    sumr=ball_a.radius+ball_b.radius
    d = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
    if d<=ball_b.radius+ball_a.radius:
        print("collide")
        return True
    else:
        return False
def check_all_balls_collision():
    for ball_a in Balls:
        for ball_b in Balls:
            if(collide(ball_a,ball_b)):
                ball_ar=ball_a.radius
                ball_br=ball_b.radius
                random_x= random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS) 
                random_y= random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
                random_dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                random_dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                color= (random.random(), random.random(), random.random())
                if ball_ar<ball_br:
                    ball_a.goto(x,y)
                    ball_a.dx=dx
                    ball_a.dy=dy
                    ball_a.color(color)
                    ball_a.radius=radius
                    ball_a.shapesize(radius/10)

                    if ball_a.radius >= MAXIMUM_BALL_RADIUS:
                        ball_b.radius=ball_b.radius+1
                        ball_b.shapesize(ball_b.radius/10)
                if ball_br<ball_ar:
                    ball_b.goto(x,y)
                    ball_b.dx=dx
                    ball_b.dy=dy
                    ball_b.color(color)
                    ball_b.radius=radius
                    ball_b.shapesize(radius/10)

                    if ball_b.radius >= MAXIMUM_BALL_RADIUS:
                        ball_a.radius=ball_a.radius+1
                        ball_b.shapesize(ball_a.radius/10)



def check_myball_collision():
    global My_Ball
    for Ball1 in Balls:

        random_x= random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS) 
        random_y= random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
        random_dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
        random_dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
        radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
        color= (random.random(), random.random(), random.random())
        if(collide(Ball1,My_Ball)):
            Ball1r=Ball1.radius
            My_Ballr=My_Ball.radius
            if My_Ballr<Ball1r:
                return False
            if Ball1r<My_Ballr:
                Ball1.goto(x,y)
                Ball1.dx=dx
                Ball1.dy=dy
                Ball1.color(color)
                Ball1.radius=radius
                Ball1.shapesize(Ball1.radius/10)
                My_Ball.radius=My_Ball.radius+1
                return True
    return True
def movearound(event):
    My_Ball.x=event.x- SCREEN_WIDTH
    My_Ball.y=SCREEN_HEIGHT -event.y
    My_Ball.goto(My_Ball.x,My_Ball.y)

turtle.getcanvas().bind("<Motion>", movearound)
getscreen().listen()


while RUNNING:
    print("running = true")
    if SCREEN_WIDTH != int(turtle.getcanvas().winfo_width()/2) or SCREEN_HEIGHT != int(turtle.getcanvas().winfo_height()/2):
        SCREEN_WIDTH= int(turtle.getcanvas().winfo_width()/2)
        SCREEN_HEIGHT= int(turtle.getcanvas().winfo_height()/2)
    move_all_balls()
    check_all_balls_collision()
    RUNNING= check_myball_collision()
    turtle.getscreen().update()
    time.sleep(SLEEP)



mainloop()