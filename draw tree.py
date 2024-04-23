import turtle
import time

t= turtle.Turtle()
turtle.bgcolor("black")
turtle.title("2D Tree")
t.shape ("circle")
t.pen(pencolor="green",fillcolor="purple", pensize=4, speed= 1)

def draw_tree(size):
    #begin head 
    t.begin_fill()
    t.fillcolor("green")

    t.circle(size)
    size+=10

    t.end_fill()

    #end head

    #begin body
    t.fillcolor("purple")

    t.goto(10,0)

    t.begin_fill()
    t.right(90)
    t.forward(size*2)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(size*2)
    t.right(90)
    t.goto(10,0)

    t.end_fill()

    #end body

    #penup=jump without drawing 
    t.penup()
    t.right(360)
    t.forward(200)

    time.sleep(2)
    exit()


draw_tree(120)   
