from src.obj.statistics import Statistics
from src.display.fonts import *
import ext.ptext as ptext



class StatisticsDrawer:
  def __init__(self, statistics: Statistics) -> None:
      self.statistics = statistics

  # Draws the score
  def draw(self) -> None:
    ptext.draw(
      str(self.statistics.score), 
      center=ORIGINAL_FONT_CENTER,
      fontname=ORIGINAL_FONT_PATH,
      fontsize=ORIGINAL_FONT_SIZE,
      owidth=ORIGINAL_FONT_OUTLINE_WIDTH, 
      ocolor=BLACK,
      shadow=ORIGINAL_FONT_SHADOW, 
      scolor=BLACK,
      color=WHITE
    )
