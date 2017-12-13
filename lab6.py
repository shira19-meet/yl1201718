from turtle import *
import random
import math
colormode(255) 
width = 100
hight = 200
def random_color(self):
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    self.color((r,g,b))


class Ball(Turtle):
    def __init__(self,radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)
ball = Ball(20,"blue",60)
ball1 = Ball(50,"pink",27)
ball.goto(100,4)
def check_collision(ball,ball1):
    x1=ball.xcor()
    x2=ball1.xcor()
    y1=ball.xcor()
    y2=ball1.xcor()
    d = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    if d>ball1.radius+ball.radius:
        print("the balls do not collide")       
    else:
        #if 
        random_color(ball)
        random_color(ball1)
        if ball.radius>ball1.radius:
            
check_collision(ball,ball1)




if ball.radius + ball.xcor() > width:
    print("the ball got to the edge")
    quit()
if ball.radius + ball.xcor() > hight:
    print("the ball got to the edge")
    quit()
if ball.radius + ball.xcor() == width:
    print("the ball got to the edge")
    quit()
if ball.radius + ball.xcor() == hight:
    print("the ball got to the edge")
    quit()

if ball.radius + ball.ycor() > width:
    print("the ball got to the edge")
    quit()
if ball.radius + ball.ycor() > hight:
    print("the ball got to the edge")
    quit()
if ball.radius + ball.ycor() == width:
    print("the ball got to the edge")
    quit()
if ball.radius + ball.ycor() == hight:
    print("the ball got to the edge")
    quit()








mainloop()

