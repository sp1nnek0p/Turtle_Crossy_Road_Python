from turtle import Turtle
import random

class Car(Turtle):
  """
  When instantiating the Class you can make this a two way game by specifying the 
  bool is_two_way=True and move_left
  is_two_way = default False
  move_left = default True set to False if moving opisite direction

  This was implemented to add dificuly on later levels
  """
  def __init__(self, is_two_way=False, move_left=True):
    super().__init__()
    self.is_two_way = is_two_way
    self.move_left = move_left
    self.car_colors = ['green', 'blue', 'red', 'yellow', 'purple', 'orange', 'cyan', 'magenta']
    
    if self.move_left:
      self.move_speed = 10
    else:
      self.move_speed = -10
    
    if self.is_two_way:
      self._get_two_way()
    else:
      self._get_one_way()
    self._create_car()


  def _get_one_way(self):
    """
    Private Method, setting the random starting positions
    if this is a one way game the cars will fill the board 
    moving in 1 direction towards left
    """
    self.random_y = random.randrange(-240, 240, 20)
    self.random_x = random.randrange(420, 1820, 70)
    self.car_color = random.choice(self.car_colors)


  def _get_two_way(self) -> None:
    """
    Private Method, setting the random starting positions
    if this is a two way game then the traffic will 
    flow in both directions
    """
    if self.move_left:
      self.random_y = random.randrange(40, 240, 20)
      self.random_x = random.randrange(420, 1820, 70)
    else:
      self.random_y = random.randrange(-240, -40, 20)
      self.random_x = random.randrange(-420, -1820, -70)

    self.car_color = random.choice(self.car_colors)


  def _create_car(self) -> None:
    """
    Private Method, used when creating the car and movint to it's starting position
    """
    self.penup()
    self.shape('square')
    self.shapesize(stretch_wid=1, stretch_len=2)
    self.color(self.car_color)
    self.goto(self.random_x, self.random_y)

  
  def move_car(self) -> None:
    """
    Start Moving the car and once the car reaches the oppisite side
    reset to a new random position
    """
    x = self.xcor() - self.move_speed
    self.goto(x, self.random_y)

    if self.xcor() < -420 and self.move_left:
      self.reset_car()
    if self.xcor() > 420 and not self.move_left:
      self.reset_car()


  def reset_car(self) -> None:
    """
    Reset the car to a new random position
    """
    if self.is_two_way:
      self._get_two_way()
    else:
      self._get_one_way()
    self.goto(self.random_x, self.random_y)


  def increase_speed(self) -> None:
    """
    Increase the speed of the turtle once he made accross the busy street
    """
    self.move_speed *= 1.2

