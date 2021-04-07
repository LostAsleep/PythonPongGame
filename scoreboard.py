from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        """Initalize the scoreboard."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update and print the current scores at the top."""
        self.clear()  # Otherwise the update numbers will overlap.
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increase left points and update scoreboard."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increase right points and update scoreboard."""
        self.r_score += 1
        self.update_scoreboard()        
