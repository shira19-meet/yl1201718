import turtle


turtle.speed(1000)
size = 50

turtle.addshape("balloon.gif")
turtle.shape("balloon.gif")
for i in range (360):
    turtle.right(i)
    turtle.forward(6*size)
    turtle.right(50)
    turtle.forward(2*size)
    turtle.right(70)
    turtle.forward(size)
    turtle.home()

turtle.mainloop()