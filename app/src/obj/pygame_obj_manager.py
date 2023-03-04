from typing import List
from src.display.bird_drawer import BirdDrawer


# Manages the storage of every pygame related object in the game
class PygameObjectManager:
  def __init__(self) -> None:
    self.birds_drawers = []

  # Stores a bird drawer
  def add_bird_drawer(self, bird_drawer: BirdDrawer) -> None:
    self.birds_drawers.append(bird_drawer)

  # Returns all bird drawers
  def get_birds_drawers(self) -> List[BirdDrawer]:
    return self.birds_drawers
