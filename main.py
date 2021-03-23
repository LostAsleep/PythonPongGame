import turtle
import time
from paddle import Paddle
from ball import Ball


def main():
    """The main function of the pong game."""
    screen = turtle.Screen()             # First create the game screen.
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

    game_is_on = True
    while game_is_on:     # The main game loop.
        screen.update()   # Refresh the contents on screen.
        time.sleep(0.01)  # The speed of the game.

    screen.exitonclick()


if __name__ == "__main__":
    main()
