import pygame

from src.obj.pipe import Pipe
from src.images import PIPE_IMG
from src.constants import *


# Class in charge of drawing a pipe
class PipeDrawer:
  PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
  PIPE_BOT = PIPE_IMG

  def __init__(self, pipe: Pipe) -> None:
    self.pipe = pipe

    self.top = self.pipe.y - self.PIPE_TOP.get_height() - PIPE_GAP / 2
    self.bot = self.pipe.y + PIPE_GAP / 2

  # Draws the pipe
  def draw(self, win: pygame.Surface) -> None:
    # Draw top
    win.blit(self.PIPE_TOP, (self.pipe.x, self.top))
    # And bottom
    win.blit(self.PIPE_BOT, (self.pipe.x, self.bot))
