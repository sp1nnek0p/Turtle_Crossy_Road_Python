from turtle import Screen, Turtle
from car import Car
from player import Player
from score import Score
from road import Road
import time
import random

# TODO: [✔] List
# TODO: Update the Levels once the other side has been reached [✔]
# TODO: Game Over when in contact with a Car [✔]
# TODO: Create the roads. [✔]
# TODO: Increase the Speed of the cars [✔]
# TODO: Increase the dificulty two a 2 lane game [✔]
# TODO: Add a way to restart the game without exiting the game [✔]

screen = Screen()
is_game_running = True
is_more_cars = False

def reset_game():
  global is_game_running, is_more_cars
  screen.reset()
  screen.clear()
  is_game_running = True
  is_more_cars = False
  main()

def main():
  global is_game_running, is_more_cars


# Setup the screen
  screen.bgcolor('#2f2f2f') # Dark Grey
  screen.tracer(0)
  screen.setup(width=800, height=600)

  road = Road()
  road.draw_roads()

  screen.listen()
  player = Player()
  score = Score()

  cars = []
  # Create 50 single way cars Class Supports 1 way or two way
  for _ in range(50):
    c = Car(is_two_way=True, move_left=random.randint(0,1))
    cars.append(c)

  # Main game loop
  while is_game_running:
    time.sleep(0.1)
    screen.update()
    screen.onkeypress(player.move_up, 'Up')
    screen.onkeypress(reset_game, 'Return' )
    for car in cars:
      car.move_car()
      if car.distance(player) < 20:
        is_game_running = False
        score.game_over()

    # if the player reached the top of the screen move him to the bottom
    # and increase the level
    if player.ycor() > 280:
      for car in cars:
        car.increase_speed()
      player.reset_player()
      score.increase_level()
    
 
    if score.level == 6 and not is_more_cars:
      for _ in range(20):
        car = Car(is_two_way=True, move_left=random.randint(0,1))
        cars.append(car)
      is_more_cars = True

# Eventlisteners

main()

screen.exitonclick()