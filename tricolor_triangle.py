import turtle

arrow = turtle.Turtle()
arrow.speed(1)

for steps in range(100):
    for c in ('red', 'blue', 'green'):
        arrow.color(c)
        arrow.forward(steps)
        arrow.right(30)

    arrow.begin_fill()
    arrow.fillcolor('red')
    for step in range(2):
        arrow.forward(100)
        arrow.left(90)
    arrow.end_fill()

    arrow.begin_fill()
    arrow.fillcolor('blue')
    for step in range(2):
        arrow.forward(100)
        arrow.left(90)
    arrow.end_fill()        

    arrow.begin_fill()
    arrow.fillcolor('green')
    for step in range(2):
        arrow.forward(100)
        arrow.left(90)
    arrow.end_fill()  

input('Testing 123: ')

arrow.forward(100)

turtle.done()
