from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_cor = choice([10, -10])
        self.y_cor = choice([10, -10])
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_cor *= -1

    def bounce_x(self):
        self.x_cor *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
