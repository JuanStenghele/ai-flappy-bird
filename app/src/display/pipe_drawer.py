import pygame

from math import floor
from src.obj.pipe import Pipe
from src.images import PIPE_IMG
from src.constants import *


# Class in charge of drawing a pipe
class PipeDrawer:
  def __init__(self, pipe: Pipe) -> None:
    self.pipe = pipe

  # Draws the pipe
  def draw(self, win: pygame.Surface) -> None:
    # draw top
    win.blit(self.pipe.PIPE_TOP, (self.pipe.x, self.pipe.top))
    # draw bottom
    win.blit(self.pipe.PIPE_BOTTOM, (self.pipe.x, self.pipe.bottom))
