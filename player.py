from turtle import Turtle


class Player(Turtle):
    def __init__(self, position=(350, 0)):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("green")
        self.shapesize(5, 1)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 15
        self.goto(self.xcor(), new_y)
