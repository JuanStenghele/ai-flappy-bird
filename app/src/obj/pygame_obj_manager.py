from typing import List
from src.display.bird_drawer import BirdDrawer
from src.display.pipe_drawer import PipeDrawer
from src.display.base_drawer import BaseDrawer
from src.display.statistics_drawer import StatisticsDrawer
from src.obj.bird import Bird
from src.obj.pipe import Pipe


# Manages the storage of every pygame related object in the game
class PygameObjectManager:
  def __init__(self) -> None:
    self.birds_drawers = []
    self.pipes_drawers = []
    self.base_drawer = None
    self.statistics_drawer = None

  def add_bird_drawer(self, bird_drawer: BirdDrawer) -> None:
    self.birds_drawers.append(bird_drawer)

  # Deletes a bird drawer
  def delete_bird_drawer(self, bird_drawer: BirdDrawer) -> None:
    self.birds_drawers.remove(bird_drawer)

  def get_birds_drawers(self) -> List[BirdDrawer]:
    return self.birds_drawers

  def add_pipe_drawer(self, pipe_drawer: PipeDrawer) -> None:
    self.pipes_drawers.append(pipe_drawer)

  # Deletes a pipe drawer
  def delete_pipe_drawer(self, pipe_drawer: PipeDrawer) -> None:
    self.pipes_drawers.remove(pipe_drawer)

  def get_pipes_drawers(self) -> List[PipeDrawer]:
    return self.pipes_drawers

  def set_base_drawer(self, base_drawer: BaseDrawer) -> None:
    self.base_drawer = base_drawer

  def get_base_drawer(self) -> BaseDrawer:
    return self.base_drawer

  def set_statistics_drawer(self, statistics_drawer: StatisticsDrawer) -> None:
    self.statistics_drawer = statistics_drawer

  def get_statistics_drawer(self) -> StatisticsDrawer:
    return self.statistics_drawer

  def get_bird_drawer(self, bird: Bird) -> BirdDrawer:
    return [drawer for drawer in self.birds_drawers if drawer.bird == bird][0]

  def get_pipe_drawer(self, pipe: Pipe) -> PipeDrawer:
    return [drawer for drawer in self.pipes_drawers if drawer.pipe == pipe][0]
