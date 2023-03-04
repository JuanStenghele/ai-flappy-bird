import pygame

from src.constants import *

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(GAME_NAME)

from src.obj.pygame_obj_manager import PygameObjectManager
from src.images import *


# Class in charge of drawing all the pygame sprites
class Drawer:
  def __init__(self, pygame_obj_manager: PygameObjectManager) -> None:
    self.win = WIN
    self.pygame_obj_manager = pygame_obj_manager

  def draw_window(self) -> None:
    self.win.blit(BG_IMG, (0,0))

    bird_drawers = self.pygame_obj_manager.get_birds_drawers()
    for drawer in bird_drawers:
      drawer.draw(self.win)

    pygame.display.update()
