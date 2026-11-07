from turtle import Turtle

MOVE_DISTANCE = 20
LIMIT = 240


class Paddle(Turtle):
    """Create a paddle and move it up/down"""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < LIMIT:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > -LIMIT:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
