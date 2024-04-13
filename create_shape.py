import turtle
arrow= turtle.Turtle()
arrow.speed(2) #slow
arrow.color("green") #extendable colours
size= 60 #interchangable

for i in range(12): #for loop runs X times 
    
    arrow.forward(size)
    arrow.right(30)


turtle.done()
