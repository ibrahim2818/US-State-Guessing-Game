from turtle import Turtle

#creating a hidden turtle which will go to the position and write the name
class Pointer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        
    def write_name(self, name, position):
        self.goto(position)
        self.write(name, move= False, align= "center", font= ("Arial", 8, "normal"))
