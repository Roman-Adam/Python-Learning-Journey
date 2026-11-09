from turtle import Screen
import time
from day23_player import Player
from day23_car_manager import Carmanager
from day23_scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = Carmanager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_it_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_increase()

screen.exitonclick()
