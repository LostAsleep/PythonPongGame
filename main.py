import turtle
import time


def main():
    """The main function of the pong game."""
    screen = turtle.Screen()             # First create the game screen.
    screen.setup(width=800, height=600)  # With it's dimensions.
    screen.bgcolor("black")              # Set the background color.
    screen.title("A Pong Game")
    screen.tracer(0)  # No automatic refreshing of the stuff on screen.

    paddle = turtle.Turtle()  # The first paddle
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x=350, y=1)

    def go_up():
        new_y = paddle.ycor() + 20
        paddle.goto(x=paddle.xcor(), y=new_y)

    def go_down():
        new_y = paddle.ycor() - 20
        paddle.goto(x=paddle.xcor(), y=new_y)

    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")

    game_is_on = True
    while game_is_on:     # The main game loop.
        screen.update()   # Refresh the contents on screen.
        time.sleep(0.02)  # The speed of the game.

    screen.exitonclick()


if __name__ == "__main__":
    main()
