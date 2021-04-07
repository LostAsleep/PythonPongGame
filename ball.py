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
        self.move_speed = 0.1

    def move(self):
        """The initial movement."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        """Reverse y direction if wall is hit.
        Bounce at 90 degree angle."""
        self.y_move *= -1
        if self.y_move > 0:
            self.y_move = 10
        if self.y_move < 0:
            self.y_move = -10

    def bounce_x(self):
        """Reverse x direction if a paddle is hit and increase speed."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Restart with ball in opposite direction and reset speed."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.y_move = 10
        self.bounce_x()