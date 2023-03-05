from typing import List
from src.obj.bird import Bird
from src.obj.pipe import Pipe


# Manages the storage of every object in the game
class ObjectManager:
  def __init__(self) -> None:
    self.birds = []
    self.pipes = []
    self.floor = None

  # Stores a bird
  def add_bird(self, bird: Bird) -> None:
    self.birds.append(bird)

  # Returns all birds
  def get_birds(self) -> List[Bird]:
    return self.birds

  # Stores a pipe
  def add_pipe(self, pipe: Pipe) -> None:
    self.pipes.append(pipe)

  # Returns all pipes
  def get_pipes(self) -> List[Pipe]:
    return self.pipes
