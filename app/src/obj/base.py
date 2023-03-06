from src.constants import *


# Class that represents a base (or floor) in the game
class Base:
  def __init__(self, y: float) -> None:
    self.y = y
    self.x = WIN_WIDTH

  # Moves the base horizontally
  def move(self) -> None:
    self.x -= WIN_WIDTH / BASE_SPEED

    if self.x <= 0:
      self.x = WIN_WIDTH
