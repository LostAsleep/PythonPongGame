from turtle import Turtle


class Ball(Turtle):
    """The ball of the pong game."""

    def __init__(self):
        """Initialize a white circle shaped ball objetct."""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """The initial movement."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        """Reverse direction if wall is hit."""
        self.y_move *= -1