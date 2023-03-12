import pygame

from math import floor
from src.obj.bird import Bird
from src.display.images import BIRD_IMGS
from src.constants import *


# Class in charge of drawing a bird
class BirdDrawer:
  IMGS = BIRD_IMGS

  def __init__(self, bird: Bird) -> None:
    self.bird = bird
    self.fly_anim_tick = 0
    self.img = self.IMGS[0]

  # Draws the bird
  def draw(self, win: pygame.Surface) -> None:
    # Flying animation update
    x: int = floor(self.fly_anim_tick / BIRD_ANIM_TRANSITION_TICKS)
    if x == 3:
      self.img = self.IMGS[1]
    else:
      self.img = self.IMGS[x]
      
    self.fly_anim_tick += 1
    # Reset amimation case
    if self.fly_anim_tick == 20:
      self.fly_anim_tick = 0

    # If the bird is diving do not move the wings
    if self.bird.tilt <= BIRD_DIVING_ROT:
      self.img = self.IMGS[1]
      # Move to IMGS[2]
      self.fly_anim_tick = BIRD_ANIM_TRANSITION_TICKS * 2

    # Tilt the bird
    rotated_image = pygame.transform.rotate(self.img, self.bird.tilt)
    new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.bird.x, self.bird.y)).center)

    # Draw the bird
    win.blit(rotated_image, new_rect.topleft)

  # Returns the y coord of the mask center
  def get_mask_center_y(self) -> float:
    return self.bird.y + self.img.get_height() / 2
