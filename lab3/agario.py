
import turtle
import random
import time
from personalproject import Ball

tracer(0)
hideturtle()
boolean=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
My_Ball=Ball(29,"black",20,16,3,7)
My_Ball.Move(400,300)
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

def random_color(self):
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    self.color((r,g,b))
Balls=[]
for i in range (NUMBER_OF_BALLS):
    x= random.randint(SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS) 
    y= random.randint(SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color=random.random(0,225)
    Ball=Ball(x,y,dx,dy,radius,color)
    Balls.append(Ball)

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
    d = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    if d>=ball_b.radius+ball_a.radius:
        return True
    else:
        return False
def check_all_balls_collision():
    for ball_a in Balls:
        for ball_b in Balls:
            if(collide(ball_a,ball_b)):
                ball_ar=ball_a.radius
                ball_br=ball_b.radius
                x= random.randint(SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS) 
                y= random.randint(SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
                dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                color=random.random(0,225)
                if ball_ar<ball_br:
                    ball_a.goto(x,y)
                    ball_a.dx=dx
                    ball_a.dy=dy
                    ball_a.color(color)
                    ball_a.radius=radius
                    ball_a.shapesize(radius/10)
                    ball_b.radius=ball_b.radius+1
                if ball_br<ball_ar:
                    ball_b.goto(x,y)
                    ball_b.dx=dx
                    ball_b.dy=dy
                    ball_b.color(color)
                    ball_b.radius=radius
                    ball.b.shapesize(radius/10)
                    ball_a==ball_a+1



def check_myball_collision():
    for Ball1 in Balls:
        if(collide(Ball1,My_Ball)):
            Ball1r=Ball1.radius
            My_Ball=MY_Ball.radius



mainloop()