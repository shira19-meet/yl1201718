import turtle
for i in range (5):
    turtle.left(145)
    turtle.forward(50)
    
turtle.register_shape("bish" , ((50,50) , (100,50) , (50,0)))
turtle.register_shape("pentagon", ((50,0), (50,50), (25,75), (0,50), (0,0)))
turtle.shape("pentagon")
turtle.right(95)
turtle.mainloop()

