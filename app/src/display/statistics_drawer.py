import pygame

from src.obj.statistics import Statistics
from src.constants import *



class StatisticsDrawer:
  def __init__(self, statistics: Statistics) -> None:
      self.statistics = statistics

  # Draws the score
  def draw(self, win: pygame.Surface) -> None:
    score_label = STAT_FONT.render("Score: " + str(self.statistics.score),1,(255,255,255))
    win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

