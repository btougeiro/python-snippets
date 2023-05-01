from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.setheading(90)
    t.forward(10)


def move_left():
    t.setheading(180)
    t.forward(10)


def move_right():
    t.setheading(0)
    t.forward(10)


def move_down():
    t.setheading(270)
    t.forward(10)


def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


s.listen()

s.onkeypress(move_forward, 'Up')
s.onkeypress(move_left, 'Left')
s.onkeypress(move_right, 'Right')
s.onkeypress(move_down, 'Down')
s.onkeypress(clear_screen, 'c')

s.exitonclick()
