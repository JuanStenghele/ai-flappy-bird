import pygame

from src.obj.pipe import Pipe
from src.images import PIPE_TOP, PIPE_BOT
from src.constants import *


# Class in charge of drawing a pipe
class PipeDrawer:
  PIPE_TOP = PIPE_TOP
  PIPE_BOT = PIPE_BOT

  def __init__(self, pipe: Pipe) -> None:
    self.pipe = pipe

    self.top = self.pipe.y - PIPE_GAP / 2
    self.bot = self.pipe.y + PIPE_GAP / 2

  # Draws the pipe
  def draw(self, win: pygame.Surface) -> None:
    # Draw top
    win.blit(self.PIPE_TOP, (self.pipe.x, self.top - self.PIPE_TOP.get_height()))
    # And bottom
    win.blit(self.PIPE_BOT, (self.pipe.x, self.bot))

  # Returns if the pipe is out of screen or not
  def is_out_of_screen(self) -> bool:
    return self.pipe.x + self.PIPE_TOP.get_width() < 0

  def update_passed(self):
    if self.pipe.x + self.PIPE_TOP.get_width() < BIRD_INITIAL_X:
      self.pipe.passed = True
