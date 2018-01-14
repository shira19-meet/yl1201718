from turtle import *
import random
import math
colormode(255) 

def random_color(self):
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    self.color((r,g,b))

class rectangle(Turtle):
    def__init__(self,speed,height,width,color):
    Turtle.__init__(self)