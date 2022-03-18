import random
import time
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            car = Turtle("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            car.penup()
            car.goto(300, y)
            self.cars.append(car)

    def move(self):
        for i in self.cars:
            i.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
