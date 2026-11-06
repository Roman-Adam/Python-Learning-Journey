import time
from turtle import Screen

from snake import Snake
from controls import Controls
from food import Food
from scoreboard import Scoreboard
from wall import Wall
from tail import Tail

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
controls = Controls(screen, snake)
food = Food()
scoreboard = Scoreboard()
wall = Wall()
tail = Tail()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Food collision
    if food.is_collision(snake.head):
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Wall collision
    if wall.is_collision(snake.head):
        game_is_on = False
        scoreboard.game_over()

    # Tail collision
    if tail.is_collision(snake):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
