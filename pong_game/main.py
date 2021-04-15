from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# move left paddle
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

# move right paddle
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect ball collision
    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.bounce_y()

    # detect paddle collision
    if (ball.distance(r_paddle) < 50) and (ball.xcor() > 320) or \
            (ball.distance(l_paddle) < 50) and (ball.xcor() < -320):
        ball.bounce_x()

    # detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
