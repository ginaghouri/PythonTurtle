# Methods of 'arrow'
# left(degrees) -> degrees represent the number of degrees to turn left
# right(degrees) -> number of degrees to turn right
# forward(x) -> move forward 'x' number of steps in the direction which the arrow is facing
# color('color name') -> change the color of the upcoming lines
# speed(1-10) -> Set the speed of the arrow
# home() -> Go back to the starting position
# begin_fill() -> start color filling process
# end_fill() -> end color filling process
# fill_color('color name') -> specify the fill color

import turtle

arrow = turtle.Turtle()
arrow.speed(1)

for steps in range(100):
    for c in ('blue', 'red', 'green'):
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

input('Testing 123: ')

arrow.forward(100)

turtle.done()
