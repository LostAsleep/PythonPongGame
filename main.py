import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def main():
    """The main function of the pong game."""
    screen = Screen()                    # First create the game screen.
    screen.setup(width=800, height=600)  # With it's dimensions.
    screen.bgcolor("black")              # Set the background color.
    screen.title("A Pong Game")
    screen.tracer(0)  # No automatic refreshing of the stuff on screen.

    l_paddle = Paddle(x_coord=-350, y_coord=0)  # The left paddle.
    r_paddle = Paddle(x_coord=350, y_coord=0)   # The right paddle.

    screen.listen()  # To enable keyboard control.
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")

    ball = Ball()
    scoreboard = Scoreboard()

    game_is_on = True
    while game_is_on:     # The main game loop.
        screen.update()   # Refresh the contents on screen.
        time.sleep(ball.move_speed)   # The speed of the game.
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddles.
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # Detect when right paddle misses.
        # Reset with ball direction to the left.
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        # Detect when left paddle misses.
        # Reset with ball direction to the right.
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

    screen.exitonclick()


if __name__ == "__main__":
    main()