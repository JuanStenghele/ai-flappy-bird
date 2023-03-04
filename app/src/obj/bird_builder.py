from src.obj.bird import Bird
from src.obj.obj_manager import ObjectManager
from src.obj.pygame_obj_manager import PygameObjectManager
from src.display.bird_drawer import BirdDrawer


# Class in charge of building a bird
class BirdBuilder:
  def __init__(self, obj_manager: ObjectManager, pg_obj_manager: PygameObjectManager) -> None:
    self.obj_manager = obj_manager
    self.pg_obj_manager = pg_obj_manager
  
  def build(self, x: float, y: float) -> Bird:
    bird = Bird(x, y)
    self.obj_manager.add_bird(bird)
    drawer = BirdDrawer(bird)
    self.pg_obj_manager.add_bird_drawer(drawer)
    return bird
