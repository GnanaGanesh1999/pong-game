from turtle import Turtle

MOVE_DISTANCE = 25


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        y_cor = self.ycor()
        if y_cor >= 240:
            return
        new_y = y_cor + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        y_cor = self.ycor()
        if y_cor <= -240:
            return
        new_y = y_cor - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
