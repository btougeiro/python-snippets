import turtle
import random

turtle.colormode(255)

color_list = [(101, 71, 64), (185, 172, 110), (64, 52, 49), (95, 115, 118), (206, 210, 138), (74, 59, 58),
              (211, 96, 71), (146, 151, 82), (231, 231, 175), (121, 148, 151), (85, 68, 70), (92, 107, 106),
              (110, 136, 138), (63, 51, 53), (74, 58, 60), (124, 148, 147), (75, 68, 45), (112, 136, 135), (55, 58, 56),
              (56, 57, 59), (61, 65, 63), (62, 63, 65), (61, 65, 66)]

billy = turtle.Turtle()
billy.penup()
billy.hideturtle()
billy.speed("fastest")
billy.setheading(225)
billy.forward(300)
billy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    billy.dot(20, random.choice(color_list))
    billy.forward(50)

    if dot_count % 10 == 0:
        billy.setheading(90)
        billy.forward(50)
        billy.setheading(180)
        billy.forward(500)
        billy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
