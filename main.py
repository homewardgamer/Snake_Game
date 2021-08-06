from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

screen.update()

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food)<15:
       food.refresh()
       score.increase_score()
       snake.extend()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<15:
            gameIsOn= True
            score.reset()
            snake.reset()


    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() < -290 or  snake.segments[0].ycor() > 290:
        gameIsOn= True
        score.reset()
        snake.reset()


screen.exitonclick()
