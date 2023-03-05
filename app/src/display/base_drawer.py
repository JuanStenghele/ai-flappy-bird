import pygame

from src.obj.base import Base
from src.constants import *


# Class in charge of drawing a base
class BaseDrawer:
  def __init__(self, base: Base) -> None:
    self.base = base

  # Draws the base
  def draw(self, win: pygame.Surface) -> None:
    win.blit(self.base.img, (self.base.x1, self.base.y))
    win.blit(self.base.img, (self.base.x2, self.base.y))
