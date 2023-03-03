from typing import List
from src.obj.bird import Bird


# Manages the storage of every object in the game
class ObjectManager:
  def __init__(self) -> None:
    self.birds = []
    self.pipes = []
    self.floor = None

  def add_bird(self, bird: Bird) -> None:
    self.birds.append(bird)

  def get_birds(self) -> List[Bird]:
    return self.birds