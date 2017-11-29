from turtle import * 
import random
colormode(255) 
class Square(Turtle):
	def __init__ (self,size):
		Turtle.__init__(self)
		self.shape ("square")
		self.shapesize()
	def random_color(self):
		r = random.randint(0,256)
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color((r,g,b))
		

# square1 = Square(15)
# square1.random_color()




class Hexagon(Turtle):
	def __init__ (self,size):
		Turtle.__init__(self)
		self.begin_poly()
		for i in range(6):
			self.forward(10)
			self.right(60)

		self.end_poly() 
		y = self.get_poly()
		register_shape("y",y) 
		self.shape("y")
	def random_color(self):
		red = random.randint(0,256)
		green = random.randint(0,256)
		blue = random.randint(0,256)
		self.color((red,green,blue))		
# hexagone1 = Hexagon(20)
# hexagone1.random_color()

class Rectangle(Turtle):
	def __init__ (self,width,hight):
		Turtle.__init__(self)
		register_shape("rectan",((width,0),(width,hight),(0,hight),(0,0)))
		self.shape ("rectan")
		self.shapesize()
	def random_color(self):
		re = random.randint(0,256)
		gr = random.randint(0,256)
		bl = random.randint(0,256)
		self.color((re,gr,bl))

#Rectangle1 = Rectangle(20,40)
#Rectangle1.random_color()

class Square1(Rectangle):
	def __init__ (self,size):
		Rectangle.__init__(self,size,size)
	def random_color(self):
		re1 = random.randint(0,256)
		gr1= random.randint(0,256)
		bl1 = random.randint(0,256)
		self.color((re1,gr1,bl1))

new_square =  Square1(20)
new_square.random_color()


mainloop()
