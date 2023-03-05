from src.images import *
from src.constants import *


class Base:
  def __init__(self, y: float) -> None:
    self.img = BASE_IMG
    self.y = y
    self.x1 = 0
    self.x2 = self.img.get_width()
    self.width = self.img.get_width()

  def move(self) -> None:
    self.x1 -= BASE_VEL
    self.x2 -= BASE_VEL
    if self.x1 + self.width < 0:
      self.x1 = self.x2 + self.width

    if self.x2 + self.width < 0:
      self.x2 = self.x1 + self.width
