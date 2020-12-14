from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1 = 0
        self.player_2 = 0
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def increase_player_1(self):
        self.player_1 += 1

    def increase_player_2(self):
        self.player_2 += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player_1, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player_2, align="center", font=("Courier", 80, "normal"))


