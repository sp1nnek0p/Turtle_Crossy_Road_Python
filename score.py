from turtle import Turtle

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.create_ui()

  def create_ui(self):
    self.level = 1
    self.hideturtle()
    self.penup()
    self.goto(-360, 270)
    self.color('white')
    self.update_score()

  def update_score(self):
    self.clear()
    self.write(f"LEVEL {self.level}", align='left', font=('OCR A Extended', 20, 'bold'))

  def increase_level(self):
    self.level += 1
    self.update_score()

  def game_over(self):
    self.color('Yellow')
    self.goto(0, 40)
    self.write('GAME OVER', align='center', font=('OCR A Extended', 46, 'bold'))
    self.goto(0, -60)
    self.write("PUSH ENTER TO PLAY AGAIN", align='center', font=('OCR A Extended', 20, 'bold'))
