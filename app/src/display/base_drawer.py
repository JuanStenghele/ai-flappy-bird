import pygame

from src.obj.base import Base
from src.images import BASE_IMG
from src.constants import *


# Class in charge of drawing a base
class BaseDrawer:
  def __init__(self, base: Base) -> None:
    self.base = base
    self.img = BASE_IMG

  # Draws the base
  def draw(self, win: pygame.Surface) -> None:
    x2: float = self.base.x - self.img.get_width()
    win.blit(self.img, (self.base.x, self.base.y))
    win.blit(self.img, (x2, self.base.y))
