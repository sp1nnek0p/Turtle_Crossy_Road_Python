from turtle import Turtle

class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.create_player()

  def create_player(self):
    self.hideturtle()
    self.color('green')
    self.shapesize(stretch_len=1.2, stretch_wid=1.2)
    self.penup()
    self.left(90)
    self.shape('turtle')
    self.goto(0, -280)
    self.showturtle()

  def move_up(self):
    self.forward(20)

  def reset_player(self):
    self.hideturtle()
    self.goto(0, -280)
    self.showturtle()