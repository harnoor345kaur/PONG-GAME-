import turtle
from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

# tim = Turtle()
# i=-40
# while i<=40:
#     tim.color("white")
#     tim.pencolor("black")
#     tim.shape("square")
#     tim.setpos(350,i)
#     i=+20

# paddle = Turtle()
# paddle.color("white")
# paddle.pencolor("black")
# paddle.shape("square")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.setpos(350,0)
#
# def go_up():
#     new_x = paddle.ycor() + 20
#     paddle.setpos(paddle.xcor(), new_x)
#
# def go_down():
#     new_x = paddle.ycor() - 20
#     paddle.setpos(paddle.xcor(), new_x)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

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
    ball.change_direction()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        print("Made Contact")
        ball.rebound()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("Made Contact")
        ball.rebound()

    if ball.xcor()<-380:
        ball.game_over()
        scoreboard.r_point()

    if ball.xcor()>380:
        ball.game_over()
        scoreboard.l_point()

screen.exitonclick()