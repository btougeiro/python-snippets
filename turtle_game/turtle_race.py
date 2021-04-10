from turtle import Turtle, Screen
import random

is_race_on = False
s = Screen()
s.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "blue", "green", "purple"]

user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
all_turtles = []

position = -175
for color_index in range(len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[color_index])
    t.penup()
    position += 50
    t.goto(x=-230, y=position)
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

s.exitonclick()
