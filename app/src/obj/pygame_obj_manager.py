from typing import List
from src.display.bird_drawer import BirdDrawer
from src.display.pipe_drawer import PipeDrawer


# Manages the storage of every pygame related object in the game
class PygameObjectManager:
  def __init__(self) -> None:
    self.birds_drawers = []
    self.pipes_drawers = []

  # Stores a bird drawer
  def add_bird_drawer(self, bird_drawer: BirdDrawer) -> None:
    self.birds_drawers.append(bird_drawer)

  # Returns all bird drawers
  def get_birds_drawers(self) -> List[BirdDrawer]:
    return self.birds_drawers

  # Stores a bird drawer
  def add_pipe_drawer(self, pipe_drawer: PipeDrawer) -> None:
    self.pipes_drawers.append(pipe_drawer)

  # Returns all bird drawers
  def get_pipes_drawers(self) -> List[PipeDrawer]:
    return self.pipes_drawers
