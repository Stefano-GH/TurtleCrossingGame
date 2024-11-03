from turtle import Turtle
from random import choice, randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_move_distance = 5
move_increment = 10


class CarManager():
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = starting_move_distance
    
    
    def create_car(self):
        random_change = randint(1, 6)
        if random_change == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(choice(colors))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    
    def level_up(self):
        self.car_speed += move_increment