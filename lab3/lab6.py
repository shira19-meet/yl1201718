from turtle import *
import random
import math
colormode(255) 
width = 400
hight = 300
print(screensize())

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
	def Move(self):
		currentx=self.xcor()
		currenty=self.ycor()
		self.goto(currentx+self.dx, currenty+self.dy)

ball = Ball(2,"black",30,12,1,6)
ball1 = Ball(50,"pink",60,49,2,9)
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
		random_color(ball)
		random_color(ball1)
		if ball.radius>ball1.radius:
			print("the balld collide")
			check_collision(ball,ball1)


while True:
	ball.Move()
	ball1.Move()


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


	if ball1.radius + ball1.xcor() > width:
		print("the ball got to the edge")
		quit()
	if ball1.radius + ball1.xcor() > hight:
		print("the ball got to the edge")
		quit()
	if ball1.radius + ball1.xcor() == width:
		print("the ball got to the edge")
		quit()
	if ball1.radius + ball1.xcor() == hight:
		print("the ball got to the edge")
		quit()

	if ball1.radius + ball1.ycor() > width:
		print("the ball got to the edge")
		quit()
	if ball1.radius + ball1.ycor() > hight:
		print("the ball got to the edge")
		quit()
	if ball1.radius + ball1.ycor() == width:
		print("the ball got to the edge")
		quit()
	if ball1.radius + ball1.ycor() == hight:
		print("the ball got to the edge")
		quit()








mainloop()

