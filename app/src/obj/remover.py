from src.obj.pipe import Pipe
from src.obj.bird import Bird
from src.obj.obj_manager import ObjectManager
from src.obj.pygame_obj_manager import PygameObjectManager
from src.constants import *


# Class in charge of building game objects
class Remover:
  def __init__(self, obj_manager: ObjectManager, pg_obj_manager: PygameObjectManager) -> None:
    self.obj_manager = obj_manager
    self.pg_obj_manager = pg_obj_manager

  # Deletes the given pipe
  def delete_pipe(self, pipe: Pipe) -> None:
    self.obj_manager.delete_pipe(pipe)
    pipe_drawer = self.pg_obj_manager.get_pipe_drawer(pipe)
    self.pg_obj_manager.delete_pipe_drawer(pipe_drawer)

  # Deletes the given bird
  def delete_bird(self, bird: Bird) -> None:
    self.obj_manager.delete_bird(bird)
    bird_drawer = self.pg_obj_manager.get_bird_drawer(bird)
    self.pg_obj_manager.delete_bird_drawer(bird_drawer)
