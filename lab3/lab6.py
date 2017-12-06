from turtle import *
import random
import math
colormode(255) 

def random_color(self):
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    self.color((r,g,b))


class Ball(Turtle):
    def __nit__(self,radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)
ball = (20,"blue",60)
ball1 = (50,"pink",27)

def check_collision(ball,ball1):
    x1=ball.xcor()
    x2=ball1.xcor()
    y1=ball.xcor()
    y2=ball1.xcor()
    d = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    if d>0:
        print("the balls do not collide")
    
                 
    else:
        circle.random_color()
check_collision(ball,ball1)
mainloop()

