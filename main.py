import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
Score = Scoreboard()
player = Player()
cars = CarManager()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars.cars:
        if car.distance(player) < 20:
            print("Crash")
            Score.game_over()
            game_is_on = False
    if player.ycor() > 280:
        player.level_up()
        Score.score_increment()
        cars.level_up()

    cars.create_car()
    cars.move()

screen.exitonclick()

# OWN 