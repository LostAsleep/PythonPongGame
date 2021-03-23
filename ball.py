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

    def initial_movement(self):
        new_x = self.xcor() + 4
        new_y = self.ycor() + 3
        self.goto(x=new_x, y=new_y)
