from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update()

    def update(self):
        self.write(f"Score: {self.score} ",align="center",font=("Courier",24,'normal'))

    def gameOver(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"Game Over", align="center", font=("Courier",28,'normal'))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()