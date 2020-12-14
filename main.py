from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(l_paddle) < 50 and (-320 > ball.xcor() > -340)) or \
            (ball.distance(r_paddle) < 50 and 320 < ball.xcor() < 340):
        ball.bounce_x()

    if ball.xcor() < -380:
        score.increase_player_2()
        ball.restart()
        score.update_scoreboard()

    if ball.xcor() > 380:
        score.increase_player_1()
        ball.restart()
        score.update_scoreboard()

screen.exitonclick()
