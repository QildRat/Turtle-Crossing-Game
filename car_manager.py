from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """if random number is equal to 1, create a car object and append to car_list."""
        # create car if random number is 1
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x=300, y=random.randint(-240, 240))
            self.car_list.append(new_car)

    def move(self):
        """move all in car_list to left."""
        for car in self.car_list:
            car.backward(self.move_speed)

    def speed_up(self):
        """increment move_speed by MOVE_INCREMENT."""
        self.move_speed += MOVE_INCREMENT
