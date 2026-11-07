import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from court import Court
from controls import Controls
from collision import Collision

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

court = Court()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
controls = Controls(screen, l_paddle, r_paddle)
collision = Collision()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Bounce off top and bottom wall
    if collision.wall(ball):
        ball.bounce_y()

    # Bounce off paddles
    if collision.paddle(ball, r_paddle, l_paddle):
        ball.bounce_x()

    # Right paddle misses -> left player scores
    if collision.right_miss(ball):
        ball.reset_position()
        scoreboard.l_point()

    # Left paddle misses -> right player scores
    if collision.left_miss(ball):
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
