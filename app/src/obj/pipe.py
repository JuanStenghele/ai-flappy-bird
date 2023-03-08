from src.images import *
from src.constants import *
from src.obj.bird import Bird


# Class that represents a pipe in the game
class Pipe:
  def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y

    self.passed = False

  # Moves the pipe and updates the passed attribute
  def move(self, bird: Bird) -> None:
    if self.x < bird.x:
      self.passed = True

    self.x -= PIPE_SPEED
