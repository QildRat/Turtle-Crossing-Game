import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# create turtle object
tim = Player()
# create multiple cars and move continuously.
carManager = CarManager()
# create scoreboard
scoreboard = Scoreboard()

# bind keys
screen.listen()
screen.onkey(key="Up", fun=tim.move_up)

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    carManager.create_car()
    carManager.move()

    # detect collision with cars
    for car in carManager.car_list:
        if car.distance(tim) < 25:
            game_is_on = False
            scoreboard.game_over()

    # detect when turtle reaches the other side, add level, increase speed of cars
    if tim.is_at_finish_line():
        time.sleep(0.5)
        tim.reset_pos()
        scoreboard.add_level()
        carManager.speed_up()

    # create scoreboard
    scoreboard.display_level()


screen.exitonclick()
