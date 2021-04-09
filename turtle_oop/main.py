from turtle import Turtle, Screen, colormode
import random

billy = Turtle()
billy.speed("fastest")

colormode(255)


def gen_random_colors():
    r = random.choice(range(0, 256))
    g = random.choice(range(0, 256))
    b = random.choice(range(0, 256))
    return r, g, b


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        billy.color(gen_random_colors())
        billy.circle(100)
        billy.setheading(billy.heading() + size_of_gap)


draw_spirograph(10)

screen = Screen()
screen.exitonclick()
