import random

from src.obj.bird import Bird
from src.obj.pipe import Pipe
from src.obj.base import Base
from src.obj.obj_manager import ObjectManager
from src.obj.pygame_obj_manager import PygameObjectManager
from src.display.bird_drawer import BirdDrawer
from src.display.pipe_drawer import PipeDrawer
from src.display.base_drawer import BaseDrawer
from src.constants import *


# Class in charge of building game objects
class Builder:
  def __init__(self, obj_manager: ObjectManager, pg_obj_manager: PygameObjectManager) -> None:
    self.obj_manager = obj_manager
    self.pg_obj_manager = pg_obj_manager

  # Build a bird at (x, y)
  def build_bird(self, x: float, y: float) -> Bird:
    bird = Bird(x, y)
    self.obj_manager.add_bird(bird)
    drawer = BirdDrawer(bird)
    self.pg_obj_manager.add_bird_drawer(drawer)
    return bird, drawer

  # Build a pipe at x
  def build_pipe(self, x: float) -> Pipe:
    y = random.randrange(PIPE_GAP / 2 + 50, WIN_HEIGHT - 200)
    pipe = Pipe(x, y)
    self.obj_manager.add_pipe(pipe)
    drawer = PipeDrawer(pipe)
    self.pg_obj_manager.add_pipe_drawer(drawer)
    return pipe

  # Build a base at y
  def build_base(self, y: float) -> Base:
    base = Base(y)
    self.obj_manager.set_base(base)
    drawer = BaseDrawer(base)
    self.pg_obj_manager.set_base_drawer(drawer)
    return base
