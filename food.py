from turtle import Turtle
import random
LEN = 0.75
WID = 0.75

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=LEN, stretch_wid=WID)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-275, 280)
        random_y = random.randint(-275, 265)
        self.goto(random_x, random_y)
