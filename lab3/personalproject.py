from turtle import *
import random
width = 400
hight = 300

def random_color(self):
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    self.color((r,g,b))


class Ball(Turtle):
    def __init__(self,radius, color, x,y,dx,dy):
        Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.dx=dx
        self.dy=dy
        self.goto(x,y)
    def Move(self,screen_width,screen_height):
        current_x=self.xcor()
        new_x=current_x+self.dx
        current_y=self.ycor()
        new_y=current_y+self.dy
        self.x=new_x
        self.y=new_y
        right_side_ball= new_x+self.radius
        left_side_ball= new_x-self.radius
        top_side_ball= new_y+ self.radius
        bottom_side_ball= new_y- self.radius
        self.goto(new_x,new_y)
        if (right_side_ball>=screen_width or left_side_ball<=-screen_width):
            self.dx=-self.dx
        if (top_side_ball>=screen_height or bottom_side_ball<=-screen_height):
            self.dy=-self.dy





        #self.goto(current_x+self.dx, current_y+self.dy)