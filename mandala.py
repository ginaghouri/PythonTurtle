import turtle

arrow = turtle.Turtle()

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        arrow.color(c)
        arrow.forward(steps)
        arrow.right(30)

