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
		

square1 = Square(15)
square1.random_color()

class Hexagon(Turtle):
	def __init__ (self,size):
		Turtle.__init__(self)
		self.begin_poly()
		for i in range(6):
			self.forward(10)
			self.right(60)

		self.end_poly() 
		y = self.get_poly()
		self.register_shape("y",y) 
		self.shape("y")
hexagone1 = Hexagon(20)
mainloop()
