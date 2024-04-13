import turtle
arrow= turtle.Turtle()
arrow.speed(10) #fast
arrow.color("blue") #extendable colours
size= 20 #interchangable

for i in range(36): #for loop runs 4 times 
    
    arrow.forward(size)
    arrow.right(10)

turtle.done()
