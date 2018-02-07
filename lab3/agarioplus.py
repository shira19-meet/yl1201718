from turtle import *
import turtle
import random
import time
from personalproject import Ball
import math
tracer(0)
hideturtle()
bgcolor("red")
SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)

RUNNING=True
SLEEP=0.0077
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=30
MINIMUM_BALL_DX=-3
MAXIMUM_BALL_DX=4
MINIMUM_BALL_DY=-2
MAXIMUM_BALL_DY=2



My_Ball = Ball(17,"blue", 0,0,0,0)


def random_color(self):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    self.color((r,g,b))
Balls=[]
for i in range(NUMBER_OF_BALLS):
    x1= random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS) 
    y1= random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
    dx1=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy1=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    radius1=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color1= (random.random(), random.random(), random.random())
    ball=Ball(radius1, color1, x1,y1,dx1,dy1)
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
                radius2=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                color2= (random.random(), random.random(), random.random())
                if ball_ar<ball_br:
                    ball_a.goto(random_x,random_y)
                    ball_a.dx=random_dx
                    ball_a.dy=random_dy
                    ball_a.color(color2)
                    ball_a.radius=radius2
                    ball_a.shapesize(radius2/10)

                    if ball_a.radius >= MAXIMUM_BALL_RADIUS:
                        ball_b.radius=ball_b.radius+1
                        ball_b.shapesize(ball_b.radius/10)
                if ball_br<ball_ar:
                    ball_b.goto(random_x,random_y)
                    ball_b.dx=random_dx
                    ball_b.dy=random_dy
                    ball_b.color(color2)
                    ball_b.radius=radius2
                    ball_b.shapesize(radius2/10)

                    if ball_b.radius >= MAXIMUM_BALL_RADIUS:
                        ball_a.radius=ball_a.radius+1
                        ball_b.shapesize(ball_a.radius/10)



def check_myball_collision():
    for Ball1 in Balls:

        random_x3= random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS) 
        random_y3= random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
        random_dx3=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
        random_dy3=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
        radius3=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
        color3= (random.random(), random.random(), random.random())
        if(collide(Ball1,My_Ball)):
            new_radius=My_Ball.radius+1
            new_radius2=Ball1.radius
            if My_Ball.radius < Ball1.radius:
                turtle.write("you lost...",font = ("Arial",20,"normal"))
                time.sleep(4)
                quit()
                return False
            else:
                My_Ball.radius = new_radius+1
                My_Ball.shapesize(My_Ball.radius/10)
                Ball1.goto(random_x3,random_y3)
                Ball1.dx=random_dx3
                Ball1.dy=random_dy3
                Ball1.color(color3)
                Ball1.radius=radius3
                Ball1.shapesize(Ball1.radius/10)
                print(My_Ball.radius)
    return True           


def movearound(event):
    My_Ball.x=event.x- SCREEN_WIDTH
    My_Ball.y=SCREEN_HEIGHT -event.y
    My_Ball.goto(My_Ball.x,My_Ball.y)

turtle.getcanvas().bind("<Motion>", movearound)
getscreen().listen()




while RUNNING :
    print("running = true")
    if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
        SCREEN_WIDTH= int(turtle.getcanvas().winfo_width()/2)
        SCREEN_HEIGHT= int(turtle.getcanvas().winfo_height()/2)

    if My_Ball.radius>MAXIMUM_BALL_RADIUS:
        turtle.write("you won the game! good job",font = ("Arial",18,"normal"))
        time.sleep(4)
        quit()
    move_all_balls()
    check_all_balls_collision()
    RUNNING= check_myball_collision()
    turtle.getscreen().update()
    time.sleep(SLEEP)


mainloop()