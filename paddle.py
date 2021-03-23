from turtle import Turtle


MOVEMENT_SPEED = 20


class Paddle(Turtle):
    """The Paddles of the pong game."""

    def __init__(self, x_coord, y_coord):
        """Initialize a white paddle with a rectangle shape."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x_coord, y=y_coord)

    def go_up(self):
        """Move the paddle up."""
        new_y = self.ycor() + MOVEMENT_SPEED
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        """Move the paddle down."""
        new_y = self.ycor() - MOVEMENT_SPEED
        self.goto(x=self.xcor(), y=new_y)
