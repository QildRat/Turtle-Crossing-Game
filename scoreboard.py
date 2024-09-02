from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1

    def display_level(self):
        """display current level."""
        self.hideturtle()
        self.color("white")
        self.teleport(x=-280, y=250)
        self.write(f"Level: {self.level}", False, "left", FONT)

    def add_level(self):
        """level increment by 1."""
        self.clear()
        self.level += 1

    def game_over(self):
        """display game over."""
        self.hideturtle()
        self.color("red")
        self.penup()
        self.home()
        self.write(f"GAME OVER!", False, "center", FONT)
