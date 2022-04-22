from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

class Game():
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = ScoreBoard()
        self.screen = Screen()
        self.game_is_on = True

    def run_game(self):
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()
            if self.snake.head.distance(self.food) < 15:
                self.food.position()
                self.scoreboard.increase_score()
                self.scoreboard.update_score()
                self.snake.extend()
            if (self.snake.head.xcor() > 300 or self.snake.head.xcor() < -300) or (self.snake.head.ycor() > 300 or self.snake.head.ycor() < -300):
                self.scoreboard.game_over()
                self.game_is_on = False 
            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.scoreboard.game_over()
                    self.game_is_on = False


    


















