from turtle import Screen 
from p11_player import Player
from p11_car_manager import CarManager
from p11_scoreboard import Scoreboard
import time 


# Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# Set initial settings
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")
screen.onkeypress(player.go_right, "Right")
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.game_off, "space")

# Secret moves
screen.onkeypress(player.secret_go_up, "w")


# Let's play
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()
    
    # Detect successfull crossing
    if player.ycor() > 280:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    
    # Stop the game
    if not player.game_on:
        game_on = False


screen.exitonclick()