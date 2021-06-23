from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
time_sleep = 0.5

screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()

right_player = Player()
left_player = Player(position=(-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.onkeypress(right_player.move_up, "Up")
screen.onkeypress(right_player.move_down, "Down")

screen.onkeypress(left_player.move_up, "w")
screen.onkeypress(left_player.move_down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 285 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with player
    if ball.distance(right_player) < 50 and ball.xcor() > 320 or ball.distance(left_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if ball goes out of bonds
    # Right player score + 1
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.right_point()
        time.sleep(time_sleep)

    # Left player score + 1
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.left_point()
        time.sleep(0.5)

screen.exitonclick()
