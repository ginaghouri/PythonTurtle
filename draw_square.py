import turtle
arrow= turtle.Turtle()
arrow.speed(1) #slow
arrow.color("purple") #extendable colours
size= 200 #interchangable

for i in range(4): #for loop runs 4 times 
    
    arrow.forward(size)
    arrow.right(90)

turtle.done()