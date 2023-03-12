import pygame

from src.constants import *

# Here we create a game window
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(GAME_NAME)

from src.obj.pygame_obj_manager import PygameObjectManager
from src.display.images import *


# Class in charge of drawing all the pygame sprites
class Drawer:
  def __init__(self, pg_obj_manager: PygameObjectManager) -> None:
    self.win = WIN
    self.pg_obj_manager = pg_obj_manager

  # Draws every sprite
  def draw(self) -> None:
    self.win.blit(BG_IMG, (0, 0))

    base_drawer = self.pg_obj_manager.get_base_drawer()
    base_drawer.draw(self.win)

    bird_drawers = self.pg_obj_manager.get_birds_drawers()
    for drawer in bird_drawers:
      drawer.draw(self.win)

    pipes_drawers = self.pg_obj_manager.get_pipes_drawers()
    for drawer in pipes_drawers:
      drawer.draw(self.win)

    statistics_drawer = self.pg_obj_manager.get_statistics_drawer()
    statistics_drawer.draw()

    pygame.display.update()
