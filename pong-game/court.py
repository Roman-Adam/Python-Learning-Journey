from turtle import Turtle


class Court(Turtle):
    """Draw the dashed center line"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pensize(4)
        self.draw_net()

    def draw_net(self):
        self.goto(0, 300)
        self.setheading(270)
        while self.ycor() > -300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
