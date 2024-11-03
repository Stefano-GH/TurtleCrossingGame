from turtle import Turtle 

starting_position = (0, -280)
move_distance = 10
secret_move_distance = 20


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        
        self.game_on = True
    
    
    def go_up(self):
        self.forward(move_distance)
    
    
    def go_down(self):
        self.backward(move_distance)
    
    
    def go_right(self):
        self.setheading(0)
        self.forward(move_distance)
        self.setheading(90)
    
    
    def go_left(self):
        self.setheading(180)
        self.forward(move_distance)
        self.setheading(90)
    
    
    def go_to_start(self):
        self.goto(starting_position)
    
    
    def game_off(self):
        self.game_on = False
    
    
    def secret_go_up(self):
        self.forward(secret_move_distance)