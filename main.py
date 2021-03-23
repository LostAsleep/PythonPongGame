import turtle
import time
from paddle import Paddle


def main():
    """The main function of the pong game."""
    screen = turtle.Screen()             # First create the game screen.
    screen.setup(width=800, height=600)  # With it's dimensions.
    screen.bgcolor("black")              # Set the background color.
    screen.title("A Pong Game")
    screen.tracer(0)  # No automatic refreshing of the stuff on screen.

    paddle_1 = Paddle(x_coord=350, y_coord=1)  # The first paddle

    screen.listen()
    screen.onkey(paddle_1.go_up, "Up")
    screen.onkey(paddle_1.go_down, "Down")

    game_is_on = True
    while game_is_on:     # The main game loop.
        screen.update()   # Refresh the contents on screen.
        time.sleep(0.02)  # The speed of the game.

    screen.exitonclick()


if __name__ == "__main__":
    main()
