from game import Game
game = Game()

screen = game.screen
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(game.snake.up,"Up")
screen.onkey(game.snake.down,"Down")
screen.onkey(game.snake.left,"Left")
screen.onkey(game.snake.right,"Right")
game.run_game()
screen.exitonclick()














