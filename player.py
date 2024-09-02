from turtle import Turtle

STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        """move the turtle upward."""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)

    def reset_pos(self):
        """go to starting position."""
        self.penup()
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """return True if player cross-over the finish line, otherwise return False."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
