import turtle
arrow= turtle.Turtle()

size = 99

arrow.color('red')
### For creating a circle
for i in range(36):
    arrow.right(10)
    arrow.forward(9)

arrow.color('purple')
arrow.right(77)
# For creating a triangle
arrow.forward(size)
arrow.right(144)
arrow.forward(size)
arrow.right(144)
arrow.forward(size)
arrow.right(144)
arrow.forward(size)
arrow.right(144)
arrow.forward(size)

arrow.color('blue')
arrow.right(67)
arrow.forward(48)
arrow.right(90)
arrow.forward(104)
arrow.right(90)
arrow.forward(104)
arrow.right(90)
arrow.forward(104)
arrow.right(90)
arrow.forward(58)

turtle.done()