from typing import List
from src.display.bird_drawer import BirdDrawer
from src.display.pipe_drawer import PipeDrawer
from src.display.base_drawer import BaseDrawer


# Manages the storage of every pygame related object in the game
class PygameObjectManager:
  def __init__(self) -> None:
    self.birds_drawers = []
    self.pipes_drawers = []
    self.base_drawer = None

  def add_bird_drawer(self, bird_drawer: BirdDrawer) -> None:
    self.birds_drawers.append(bird_drawer)

  def get_birds_drawers(self) -> List[BirdDrawer]:
    return self.birds_drawers

  def add_pipe_drawer(self, pipe_drawer: PipeDrawer) -> None:
    self.pipes_drawers.append(pipe_drawer)

  def get_pipes_drawers(self) -> List[PipeDrawer]:
    return self.pipes_drawers

  def set_base_drawer(self, base_drawer: BaseDrawer) -> None:
    self.base_drawer = base_drawer

  def get_base_drawer(self) -> BaseDrawer:
    return self.base_drawer
