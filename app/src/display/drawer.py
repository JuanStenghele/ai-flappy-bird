import pygame

from src.constants import *

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(GAME_NAME)

from src.obj.obj_manager import ObjectManager
from src.images import *


# Class in charge of drawing all the pygame sprites
class Drawer:
  def __init__(self, obj_manager: ObjectManager) -> None:
    self.win = WIN
    self.obj_manager = obj_manager

  def draw_window(self) -> None:
    self.win.blit(BG_IMG, (0,0))



    pygame.display.update()
