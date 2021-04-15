from turtle import Turtle

PADDLE_WID_SIZE = 5
PADDLE_LEN_SIZE = 1


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WID_SIZE, stretch_len=PADDLE_LEN_SIZE)
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
