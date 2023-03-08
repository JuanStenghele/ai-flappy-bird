from typing import List
from src.obj.bird import Bird
from src.obj.pipe import Pipe
from src.obj.base import Base
from src.obj.statistics import Statistics


# Manages the storage of every object in the game
class ObjectManager:
  def __init__(self) -> None:
    self.birds = []
    self.pipes = []
    self.base = None

  # Stores a bird
  def add_bird(self, bird: Bird) -> None:
    self.birds.append(bird)

  # Deletes a bird
  def delete_bird(self, bird: Bird) -> None:
    self.birds.remove(bird)

  # Returns all birds
  def get_birds(self) -> List[Bird]:
    return self.birds

  # Stores a pipe
  def add_pipe(self, pipe: Pipe) -> None:
    self.pipes.append(pipe)

  # Deletes a pipe
  def delete_pipe(self, pipe: Pipe) -> None:
    self.pipes.remove(pipe)

  # Returns all pipes
  def get_pipes(self) -> List[Pipe]:
    return self.pipes

  def set_base(self, base: Base) -> None:
    self.base = base

  def get_base(self) -> Base:
    return self.base

  def set_statistics(self, statistics: Statistics) -> None:
    self.statistics = statistics

  def get_statistics(self) -> Statistics:
    return self.statistics
