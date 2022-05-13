from turtle import Turtle

class Road(Turtle):
  def __init__(self):
    super().__init__()
    self.create_road()

  def create_road(self):
    self.penup()
   
    self.hideturtle()
    # self.shape('square')
    self.color('yellow')
    self.goto(400, -260)
    self.pensize(5)

  def draw_roads(self):
    self.pendown()
    self.setheading(180)
    self._move_forward()
    self.goto(self.xcor(), 260)
    self.setheading(0)
    self._move_forward()
    self.goto(self.xcor(), 20)
    self.setheading(180)
    self._move_forward()
    self.goto(self.xcor(), -20)
    self.setheading(0)
    self._move_forward()

  def _move_forward(self):
     self.forward(810)