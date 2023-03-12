from src.constants import *
from src.display.images import *


# Represents a bird in the game
class Bird:
  def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y
    self.ticks = 0
    self.tilt = 0

  # Makes the bird jump
  def jump(self) -> None:
    self.ticks = 0

  # Natural bird movement
  def move(self) -> None:
    self.ticks += 1

    # We use a UAM for the movement
    # Displacement = v0 * t +  1/2 * a * t^2
    displacement: float = BIRD_JUMP_SPEED * self.ticks + 0.5 * GRAVITY * (self.ticks ** 2)
    # We adjust displacement to avoid rough transitions
    # If we go down too fast...
    if (displacement >= BIRD_MAX_SPEED_DOWN):
      displacement = BIRD_MAX_SPEED_DOWN
    self.y += displacement

    # Adjust the tilt
    if displacement < 0:
      # Tilt up
      self.tilt = BIRD_MAX_ROT
    else:
      # Tilt down
      if self.tilt > BIRD_MIN_ROT:
        self.tilt -= BIRD_ROT_SPEED
