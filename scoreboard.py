from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.display_score = self.update_score()

    def update_score(self):
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align="center",font=("Arial", 24, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score
    
    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial", 24, "normal"))